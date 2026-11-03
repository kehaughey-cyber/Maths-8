"""
Per-node table: floor node -> claim text (name and claim columns of the M6 spine tables only) -> Lean module(s) in floor/lean_M5/lean -> theorem count -> compile result -> axiom footprint.
Reads explore/lean_M5_check*.out (compile results) and floor/M6_SPINE_2026-10-19.md (claim text).  New file (2026-11-03).  Prints markdown.
Usage:  py -3 -I -X utf8 -u explore/lean_M5_nodes.py > explore/lean_M5_nodes.out
"""
import os, re, glob
here = os.path.dirname(os.path.abspath(__file__)); repo = os.path.normpath(os.path.join(here, '..'))
spine = open(os.path.join(repo, 'floor', 'M6_SPINE_2026-10-19.md'), encoding='utf-8').read()
claims = {}
for m in re.finditer(r'^\| \*\*(\d\d)\*\* `([^`]+)` \| (.*?) \| (.*?) \|\s*$', spine, re.M):
    claims[int(m.group(1))] = (m.group(2), m.group(3))     # name and claim text only; the fourth (scope) column is not read
res = {}   # module -> dict(status, thm, sorry, axdecl, imports, axioms set, noaxiom count)
for fn in sorted(glob.glob(os.path.join(here, 'lean_M5_check*.out'))):
    cur = None
    for line in open(fn, encoding='utf-8').read().splitlines():
        m = re.match(r'^(Container\d\d\.\S+)\s+(\S+)\s+theorems\s+(\d+)\s+sorry\s+(\d+)\s+axiom-decls\s+(\d+)\s+imports\s+(.*)$', line)
        if m:
            cur = m.group(1); res[cur] = dict(status=m.group(2), thm=int(m.group(3)), sorry=int(m.group(4)), axdecl=int(m.group(5)), imports=m.group(6), axioms=set(), none=0, n_ax_lines=0)
            continue
        if cur and line.startswith('    '):
            if 'does not depend on any axioms' in line: res[cur]['none'] += 1
            m2 = re.search(r'depends on axioms: \[(.*?)\]', line)
            if m2:
                res[cur]['n_ax_lines'] += 1
                for a in m2.group(1).split(','): res[cur]['axioms'].add(a.strip())
            if 'error' in line.lower(): res[cur].setdefault('errors', []).append(line.strip()[:160])
print('| node | name | claim (M6 spine claim column) | Lean module | theorems | compile | axiom footprint of the checked theorems |')
print('|---|---|---|---|---|---|---|')
mods_by_node = {}
for mod in res: mods_by_node.setdefault(int(mod[9:11]), []).append(mod)
for node in range(0, 68):
    name, claim = claims.get(node, ('', ''))
    mods = sorted(mods_by_node.get(node, []))
    if not mods:
        print(f'| {node:02d} | {name} | {claim} | (no result) | | | |'); continue
    for mod in mods:
        r = res[mod]
        fp = ('none (zero axioms)' if not r['axioms'] and r['none'] else '') or ''
        if r['axioms']: fp = '{' + ', '.join(sorted(r['axioms'])) + '}' + (f' ({r["none"]} theorems axiom-free)' if r['none'] else '')
        if not fp: fp = 'no `#print axioms` in the file'
        print(f'| {node:02d} | {name} | {claim} | `{mod}` | {r["thm"]} | {r["status"]} | {fp} |')
