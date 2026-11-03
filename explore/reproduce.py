"""
Reproduce check for the explore/ scripts.  New file (2026-11-02).  Reads nothing but the committed repository.

What it does
  1. Exports the committed tree (git archive HEAD, i.e. what a fresh clone has) into a scratch directory, so no run can overwrite repository files.
  2. Reads every recorded sha256 of the form "*name.py <64 hex>" / "*name.out <64 hex>" from the notes in explore/*.md, maps/*.md and the top-level *.md.
  3. For each explore/<stem>.py that has a committed explore/<stem>.out, runs it from the scratch root exactly as the notes say
        py -3 -I -X utf8 -u explore/<stem>.py > explore/<stem>.out
     with a timeout, and compares the new stdout with (a) the committed .out and (b) the hash recorded in the notes, if any.
  4. Checks the exec/import chain: for each script, every explore/*.py it loads by exec(open(...)) or spec_from_file_location is listed with
     its current sha256 and the sha256 recorded for it in the notes (DEP_DRIFT if they differ), because the chain splits the loaded source at a
     marker string, and a changed dependency would silently change the result.
  5. Writes a report: explore/REPRODUCE_REPORT_<date>.md (raw status per script, environment, first differing line where output differs).
Statuses: MATCH (new == committed .out; and == recorded hash if recorded), MATCH_UNRECORDED (new == committed, no hash in notes),
          RECORD_MISMATCH (new == committed but the notes record a different hash), DIFFERS (new != committed), TIMEOUT, ERROR (nonzero exit),
          SCRIPT_DRIFT (committed script's hash != the one recorded in the notes), MARKER_MISSING (a chained source-split marker is not in the dependency).
Usage:   py -3 -I -X utf8 -u explore/reproduce.py [--timeout SEC] [--workers N] [--only substr] > explore/reproduce_run.out
"""
import os, re, sys, glob, hashlib, shutil, subprocess, tempfile, time, platform, datetime, argparse, concurrent.futures as cf

ap = argparse.ArgumentParser(); ap.add_argument('--timeout', type=int, default=1500); ap.add_argument('--workers', type=int, default=4); ap.add_argument('--only', default='')
args = ap.parse_args()
repo = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True, cwd=os.path.dirname(os.path.abspath(__file__))).strip()
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True, cwd=repo).strip()
sha = lambda b: hashlib.sha256(b).hexdigest()

# 1. fresh export of the committed tree
scratch = tempfile.mkdtemp(prefix='maths8_repro_')
tar = os.path.join(scratch, 'tree.tar'); subprocess.check_call(['git', 'archive', '--format=tar', '-o', tar, 'HEAD'], cwd=repo)
root = os.path.join(scratch, 'tree'); os.makedirs(root); subprocess.check_call(['tar', '-xf', tar, '-C', root])

# 2. recorded hashes in notes (the committed notes, from the export)
rec = {}; recfiles = {}
for md in glob.glob(os.path.join(root, '**', '*.md'), recursive=True):
    t = open(md, encoding='utf-8', errors='replace').read()
    for name, h in re.findall(r'\*([A-Za-z0-9_\-\.]+\.(?:py|out))\s+([0-9a-f]{64})', t):
        rec.setdefault(name, set()).add(h); recfiles.setdefault((name, h), os.path.relpath(md, root))

ex = os.path.join(root, 'explore')
scripts = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ex, '*.py')) if os.path.exists(p[:-3] + '.out') and os.path.basename(p) != 'reproduce.py')
scripts = [s for s in scripts if args.only in s]
run_env = dict(os.environ); run_env.pop('PYTHONPATH', None)

def deps_of(stem):
    src = open(os.path.join(ex, stem + '.py'), encoding='utf-8').read(); out = []
    for m in re.finditer(r"exec\(open\((.*?)\)\.read\(\)\.split\((['\"])(.*?)\2\)", src):
        names = re.findall(r"['\"]([A-Za-z0-9_]+\.py)['\"]", m.group(1)); out.append((names[0] if names else None, m.group(3)))
    for m in re.finditer(r"spec_from_file_location\([^,]+,\s*os\.path\.join\([^,]+,\s*['\"]([A-Za-z0-9_]+\.py)['\"]\)", src): out.append((m.group(1), None))
    return out

def check(stem):
    r = {'stem': stem, 'notes': []}
    sp = os.path.join(ex, stem + '.py'); so = os.path.join(ex, stem + '.out'); sb = open(sp, 'rb').read(); ob = open(so, 'rb').read()
    r['script_sha'] = sha(sb); r['committed_out_sha'] = sha(ob)
    if stem + '.py' in rec and r['script_sha'] not in rec[stem + '.py']: r['notes'].append('SCRIPT_DRIFT: committed script ' + r['script_sha'][:12] + ' not in recorded ' + ','.join(h[:12] for h in rec[stem + '.py']))
    for dname, marker in deps_of(stem):
        if not dname: continue
        dp = os.path.join(ex, dname)
        if not os.path.exists(dp): r['notes'].append('DEP_MISSING ' + dname); continue
        dsrc = open(dp, 'rb').read(); dh = sha(dsrc)
        if marker is not None and marker not in dsrc.decode('utf-8'): r['notes'].append('MARKER_MISSING in ' + dname + ': ' + marker[:40])
        if dname in rec and dh not in rec[dname]: r['notes'].append('DEP_DRIFT ' + dname + ' ' + dh[:12] + ' not in recorded ' + ','.join(h[:12] for h in rec[dname]))
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, '-I', '-X', 'utf8', '-u', os.path.join('explore', stem + '.py')], cwd=root, capture_output=True, timeout=args.timeout, env=run_env)
    except subprocess.TimeoutExpired:
        r['status'] = 'TIMEOUT'; r['secs'] = round(time.time() - t0, 1); return r
    r['secs'] = round(time.time() - t0, 1); r['rc'] = p.returncode; r['new_out_sha'] = sha(p.stdout)
    if p.returncode != 0: r['status'] = 'ERROR'; r['stderr_tail'] = p.stderr.decode('utf-8', 'replace').strip().splitlines()[-3:]; return r
    if p.stdout == ob:
        recout = rec.get(stem + '.out')
        r['status'] = 'MATCH_UNRECORDED' if not recout else ('MATCH' if r['new_out_sha'] in recout else 'RECORD_MISMATCH')
    else:
        r['status'] = 'DIFFERS'; a = ob.decode('utf-8', 'replace').splitlines(); b = p.stdout.decode('utf-8', 'replace').splitlines()
        for i in range(max(len(a), len(b))):
            x = a[i] if i < len(a) else '<end>'; y = b[i] if i < len(b) else '<end>'
            if x != y: r['first_diff'] = (i + 1, x[:160], y[:160]); break
    return r

print(f'reproduce.py: commit {commit}, {len(scripts)} scripts with a committed .out, scratch {scratch}'); sys.stdout.flush()
results = []
with cf.ThreadPoolExecutor(max_workers=args.workers) as exe:
    futs = {exe.submit(check, s): s for s in scripts}
    for f in cf.as_completed(futs):
        r = f.result(); results.append(r); print(f"  {r['stem']:48s} {r['status']:17s} {r.get('secs', '')}s " + ('; '.join(r['notes'])[:160] if r['notes'] else '')); sys.stdout.flush()
results.sort(key=lambda r: r['stem'])
cnt = {}
for r in results: cnt[r['status']] = cnt.get(r['status'], 0) + 1
print('\nsummary:', cnt, '| scripts with any chain/hash note:', sum(1 for r in results if r['notes']))
date = datetime.date.today().isoformat(); rp = os.path.join(repo, 'explore', f'REPRODUCE_REPORT_{date}.md')
with open(rp, 'w', encoding='utf-8') as f:
    f.write(f'# Reproduce report {date}\n\nGenerated by `explore/reproduce.py` against a fresh export of commit `{commit}` (git archive HEAD, run from the export root with the commands recorded in the notes). Raw statuses, nothing edited.\n\n')
    f.write(f'Environment: Python {platform.python_version()} ({platform.python_implementation()}), {platform.platform()}\n')
    try:
        import numpy, sympy, mpmath; f.write(f'NumPy {numpy.__version__}, SymPy {sympy.__version__}, mpmath {mpmath.__version__}\n\n')
    except Exception as e: f.write(f'(version import failed: {e})\n\n')
    f.write('Summary: ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items())) + f' (total {len(results)})\n\n')
    f.write('Status key: MATCH = new output identical to the committed .out and to the hash recorded in a note; MATCH_UNRECORDED = identical to the committed .out, no hash recorded in the notes; RECORD_MISMATCH = identical to the committed .out but a note records a different hash; DIFFERS = new output differs from the committed .out; TIMEOUT/ERROR as named.\n\n')
    f.write('| script | status | seconds | new out sha256 (12) | notes |\n|---|---|---|---|---|\n')
    for r in results: f.write(f"| {r['stem']}.py | {r['status']} | {r.get('secs', '')} | {r.get('new_out_sha', '')[:12]} | {'; '.join(r['notes'])} |\n")
    bad = [r for r in results if r['status'] not in ('MATCH', 'MATCH_UNRECORDED')]
    if bad:
        f.write('\n## Details for anything other than MATCH / MATCH_UNRECORDED\n\n')
        for r in bad:
            f.write(f"- **{r['stem']}.py** {r['status']}")
            if 'first_diff' in r: n, x, y = r['first_diff']; f.write(f" first differing line {n}:\n    - committed: `{x}`\n    - new:       `{y}`")
            if 'stderr_tail' in r: f.write(' stderr tail: ' + ' | '.join(r['stderr_tail']))
            f.write('\n')
print('report:', rp)
shutil.rmtree(scratch, ignore_errors=True)
