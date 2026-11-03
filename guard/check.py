#!/usr/bin/env python3
"""Guard for the Maths 8 repo (run with: py -3 -I guard/check.py [--all | --staged | --stdin NAME]).

Scans text for the patterns in guard/patterns.txt and checks that every floor/ file still matches the sha256
recorded in floor/PROVENANCE.md. Exit 1 if any ERROR is found. Prints file:line for every hit.
  --all     scan tracked and untracked (not ignored) files in the working tree (default)
  --staged  scan the staged versions of the files about to be committed (used by the pre-commit hook)
  --stdin NAME  scan text read from stdin as if it were the file NAME (used to test the patterns)
"""
import re, sys, subprocess, hashlib, fnmatch, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = ('.git/', 'floor/', 'explore/data/')
SKIP_EXT = {'.html', '.csv', '.xlsx', '.zip', '.npy', '.png', '.pdf', '.bin', '.out', '.json'}
MAX_BYTES = 2_000_000


def git(*args, binary=False):
    r = subprocess.run(['git', *args], cwd=ROOT, capture_output=True)
    return r.stdout if binary else r.stdout.decode('utf-8', 'replace')


def decode(b):
    if b[:2] in (b'\xff\xfe', b'\xfe\xff'):
        return b.decode('utf-16', 'replace')
    return b.decode('utf-8-sig', 'replace')


def load_cfg():
    rules, exempt = [], []
    for line in (ROOT / 'guard' / 'patterns.txt').read_text(encoding='utf-8').splitlines():
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        kind, rest = s.split(None, 1)
        if kind == 'EXEMPT':
            exempt.append(rest.strip())
        else:
            label, rx = rest.split(None, 1)
            rules.append((kind, label, re.compile(rx)))
    return rules, exempt


def scan(name, text, rules):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for sev, label, rx in rules:
            m = rx.search(line)
            if m:
                hits.append((sev, label, name, i, line.strip()[:110]))
    return hits


def floor_check(staged):
    """Every floor file must hash to the value in floor/PROVENANCE.md (working tree, or the staged blob)."""
    hits = []
    prov = (ROOT / 'floor' / 'PROVENANCE.md').read_text(encoding='utf-8', errors='replace')
    table = dict(re.findall(r'^\|\s*`([^`]+)`\s*\|\s*`[^`]+`\s*\|\s*`([0-9a-f]{64})`', prov, re.M))
    if not table:
        return [('ERROR', 'floor-table', 'floor/PROVENANCE.md', 0, 'no hash table found')]
    for fn, want in table.items():
        rel = 'floor/' + fn
        if staged and rel in git('diff', '--cached', '--name-only').split():
            data = git('show', ':' + rel, binary=True)
        else:
            p = ROOT / rel
            if not p.exists():
                hits.append(('ERROR', 'floor-missing', rel, 0, 'file listed in PROVENANCE is missing'))
                continue
            data = p.read_bytes()
        got = hashlib.sha256(data).hexdigest()
        if got != want:
            hits.append(('ERROR', 'floor-hash', rel, 0, f'sha256 {got[:16]}… != PROVENANCE {want[:16]}…'))
    return hits


def candidates(staged):
    if staged:
        names = git('diff', '--cached', '--name-only', '--diff-filter=ACMR').split('\n')
    else:
        names = git('ls-files').split('\n') + git('ls-files', '--others', '--exclude-standard').split('\n')
    return [n.strip() for n in dict.fromkeys(names) if n.strip()]


def main(argv):
    rules, exempt = load_cfg()
    hits = []
    if argv[:1] == ['--stdin']:
        hits += scan(argv[1], decode(sys.stdin.buffer.read()), rules)
    else:
        staged = argv[:1] == ['--staged']
        for n in candidates(staged):
            if n.startswith(SKIP_DIRS) or pathlib.PurePosixPath(n).suffix.lower() in SKIP_EXT:
                continue
            if any(fnmatch.fnmatch(n, e) for e in exempt):
                continue
            data = git('show', ':' + n, binary=True) if staged else (ROOT / n).read_bytes() if (ROOT / n).is_file() else b''
            if not data or len(data) > MAX_BYTES:
                continue
            hits += scan(n, decode(data), rules)
        hits += floor_check(staged)
    err = [h for h in hits if h[0] == 'ERROR']
    for sev, label, name, line, snip in hits:
        print(f'{sev:5s} {label:16s} {name}:{line}: {snip}')
    print(f'guard: {len(err)} error(s), {len(hits) - len(err)} warning(s)')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
