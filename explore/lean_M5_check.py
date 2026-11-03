"""
Compile the inherited Maths 5 Lean sources (copied byte for byte into floor/lean_M5/lean/) and record, per file: return code, messages, whether the file contains
`sorry` or `axiom`, the theorem/lemma count, and the `#print axioms` output if the file has it.  New file (2026-11-03).  Nothing is edited; compiled output goes to a scratch directory.
Toolchain: the one named in floor/lean_M5/lean/lean-toolchain, called directly from ~/.elan/toolchains (no elan resolution, no download).
Mathlib and its dependencies: read-only use of the oleans already built in Maths 5's lean/.lake/packages (path given with --pkgs); nothing is written there.
Modules whose imports have all compiled are compiled in parallel (--workers); results are printed in a fixed (import) order after all have finished, so the output does not depend on timing.
Usage:  py -3 -I -X utf8 -u explore/lean_M5_check.py --pkgs "<path to Maths 5>/lean/.lake/packages" [--workers 6] [--timeout 600] [--only substr] [--skip a,b] > explore/lean_M5_check.out
"""
import os, re, sys, subprocess, tempfile, argparse, glob, shutil, time
import concurrent.futures as cf

ap = argparse.ArgumentParser(); ap.add_argument('--pkgs', required=True); ap.add_argument('--timeout', type=int, default=600); ap.add_argument('--only', default='')
ap.add_argument('--workers', type=int, default=6); ap.add_argument('--skip', default='')
args = ap.parse_args()
skip = [s for s in args.skip.split(',') if s]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.normpath(os.path.join(here, '..', 'floor', 'lean_M5', 'lean'))
tc = open(os.path.join(root, 'lean-toolchain')).read().strip().replace('leanprover/lean4:', '')
lean = os.path.join(os.path.expanduser('~'), '.elan', 'toolchains', 'leanprover--lean4---' + tc, 'bin', 'lean.exe')
assert os.path.exists(lean), lean
libs = []
for p in sorted(os.listdir(args.pkgs)):
    d = os.path.join(args.pkgs, p, '.lake', 'build', 'lib', 'lean')
    if os.path.isdir(d): libs.append(d)
build = tempfile.mkdtemp(prefix='m5lean_')
env = dict(os.environ); env['LEAN_PATH'] = os.pathsep.join([build] + libs)
print('toolchain:', subprocess.run([lean, '--version'], capture_output=True, text=True).stdout.strip())
print('lean-toolchain file:', tc)
print('mathlib libs found:', [os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(l))))) for l in libs])
files = sorted(glob.glob(os.path.join(root, 'Container*', '*.lean')))
mods = {}
for f in files:
    rel = os.path.relpath(f, root).replace(os.sep, '/'); mod = rel[:-5].replace('/', '.')
    src = open(f, encoding='utf-8').read()
    imps = re.findall(r'^import\s+(\S+)', src, re.M)
    mods[mod] = (f, rel, src, imps)
order = []; seen = set()
def visit(m):
    if m in seen or m not in mods: return
    seen.add(m)
    for i in mods[m][3]: visit(i)
    order.append(m)
for m in sorted(mods): visit(m)
sel = [m for m in order if (not args.only or args.only in m) and not any(s in m for s in skip)]
print(f'{len(order)} modules in total, {len(sel)} selected (skipped: {skip if skip else "none"}); workers {args.workers}, timeout {args.timeout}s each\n'); sys.stdout.flush()

def compile_one(m):
    f, rel, src, imps = mods[m]
    out = os.path.join(build, rel[:-5] + '.olean'); os.makedirs(os.path.dirname(out), exist_ok=True)
    t0 = time.time()
    try:
        p = subprocess.run([lean, '-o', out, rel], cwd=root, env=env, capture_output=True, text=True, timeout=args.timeout)
        rc = p.returncode; msg = (p.stdout + p.stderr).strip()
    except subprocess.TimeoutExpired:
        rc = 'TIMEOUT'; msg = ''
    return m, rc, msg, time.time() - t0

results = {}; done = set(); pending = list(sel)
with cf.ThreadPoolExecutor(max_workers=args.workers) as exe:
    running = {}
    while pending or running:
        for m in list(pending):
            deps = [i for i in mods[m][3] if i in mods]
            if any(d in sel and d not in done for d in deps): continue
            if any(d in results and results[d][0] != 0 for d in deps):
                results[m] = ('SKIPPED_DEP_FAILED', 'a dependency did not compile', 0.0); done.add(m); pending.remove(m); continue
            running[exe.submit(compile_one, m)] = m; pending.remove(m)
        if not running: continue
        fin, _ = cf.wait(list(running), return_when=cf.FIRST_COMPLETED)
        for fu in fin:
            m, rc, msg, dt = fu.result(); results[m] = (rc, msg, dt); done.add(m); running.pop(fu)
            sys.stderr.write(f'  done {m} rc={rc} {dt:.0f}s\n'); sys.stderr.flush()

ok = bad = 0
for m in sel:
    f, rel, src, imps = mods[m]; rc, msg, dt = results[m]
    nthm = len(re.findall(r'^\s*(?:theorem|lemma)\s', src, re.M)); nsorry = len(re.findall(r'\bsorry\b', src)); naxiom = len(re.findall(r'^\s*axiom\s', src, re.M))
    status = 'OK' if rc == 0 else (rc if isinstance(rc, str) else f'FAIL({rc})')
    if rc == 0: ok += 1
    else: bad += 1
    print(f'{m:55s} {status:20s} theorems {nthm:3d} sorry {nsorry} axiom-decls {naxiom} imports {",".join(imps) if imps else "(none)"}')
    for line in msg.splitlines():
        low = line.lower()
        if 'axiom' in low or 'error' in low or 'sorry' in low or 'depends on' in low: print('    ' + line[:240])
print(f'\nsummary: {ok} compiled, {bad} not  (of {len(sel)})')
shutil.rmtree(build, ignore_errors=True)
