"""
Assemble SPINE_M8_UNIFIED_2026-11-03.md: the spine narrative (SPINE_M8_2026-11-03.md) with each part followed by its equations and proofs
(SPINE_M8_PROOFS_2026-11-03.md), plus the route-56 entry and the explicit status of what is not carried.  New file (2026-11-03).  Text is copied, not rewritten.
Usage: py -3 -I -X utf8 -u explore/build_unified_spine.py > SPINE_M8_UNIFIED_2026-11-03.md
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
repo = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
spine = open(os.path.join(repo, 'SPINE_M8_2026-11-03.md'), encoding='utf-8').read().replace('\r\n', '\n')
proofs = open(os.path.join(repo, 'SPINE_M8_PROOFS_2026-11-03.md'), encoding='utf-8').read().replace('\r\n', '\n')

def sp(prefix):               # spine block whose heading starts with prefix, up to the next heading of the same or higher level
    out = []; on = False; lvl = None
    for ln in spine.split('\n'):
        m = re.match(r'^(#+) ', ln)
        if m and not on and ln.startswith(prefix):
            on = True; lvl = len(m.group(1)); out.append(ln); continue
        if on:
            if m and len(m.group(1)) <= lvl: break
            out.append(ln)
    assert out, prefix
    return '\n'.join(out).strip()

def pr(cid):                  # proofs entry "### C-xx ..." up to the next ###, ## or ---
    m = re.search(r'(?ms)^### %s[ \n].*?(?=^### |^## |^---)' % re.escape(cid), proofs)
    assert m, cid
    return ('#' + m.group(0)).strip()          # demote one level

def demote(t): return re.sub(r'(?m)^(#+) ', lambda m: '#' + m.group(1) + ' ', t)
def block(ids): return '\n\n'.join(pr(i) for i in ids)

O = []
w = O.append
w(open(os.path.join(repo, 'explore', 'unified_spine_head.md'), encoding='utf-8').read().strip() + '\n')
w(sp('## 0. '))
w('\n---\n')
w(sp('## I. The floor'))
w('\n### Equations and proofs for Part I (container 00 to 02)\n')
w('The Lean originals of these three containers are among the imported modules (Part II table, rows 00 to 02); the entries below are the same claims proved in elementary form so a reader can check them without Lean.\n')
w(block(['C-A1', 'C-A2', 'C-A3', 'C-A4']))
w('\n---\n')
w(sp('## II. The M5 trunk'))
w('\n### Proofs for Part II (nodes 00 to 67): the Lean proofs of record\n')
m = re.search(r'(?ms)^## I\. Floor nodes 00 to 67.*?(?=^---\n\n## B\.)', proofs); assert m
sec = re.sub(r'^## I\. [^\n]*\n', '', m.group(0)).strip()
w(demote(sec))
w('\n---\n')
w('## II-b. The finite carrier, re-derived (supports Parts II, III and IV)\n')
w('The floor facts that the Maths 8 instrument rests on, proved here directly (independently of the Lean modules above, which cover the same nodes in kernel-checked form where a theorem exists).\n')
w(block(['C-B1', 'C-B2', 'C-B3', 'C-B4', 'C-B5']))
w('\n---\n')
w(sp('## III. The M6 layer'))
w(open(os.path.join(repo, 'explore', 'unified_spine_part3.md'), encoding='utf-8').read().strip())
w('\n---\n')
w("## IV. Maths 8's own work, with proofs\n")
w(sp('### IV.1 '))
w(open(os.path.join(repo, 'explore', 'unified_spine_route56.md'), encoding='utf-8').read().strip())
w('\n')
w(sp('### IV.2 '))
w('\n#### Proof entries for IV.2 (the Bekenstein-Compton dictionary)\n')
w(block(['C-C1', 'C-C2', 'C-C3', 'C-C4']))
w('\n')
w(sp('### IV.3 '))
w('\n#### Proof entries for IV.3 (alpha)\n')
w(block(['C-D1']))
w('\n')
w(sp('### IV.4 '))
w('\n**Proofs for IV.4:** none; the lab is a viewer of the maps and the spine nodes. It carries no claim of its own beyond what it displays from them.\n')
w(sp('### IV.5 '))
w("\n**Proofs for IV.5:** the critical path, the percentage frame and the carbon-gram aspects are catalogues and framings. The one computed object is the gram's BC count (C-C4 above). The 36-aspect inventory is not proved row by row (Part IX).\n")
w(sp('### IV.6 '))
w('\n#### Proof entries for IV.6 (the E-series instrument)\n')
w(block(['C-E1', 'C-E2', 'C-E3', 'C-E4', 'C-E5', 'C-E6', 'C-E7', 'C-E8']))
w('\n')
w(sp('### IV.7 '))
w('\n#### Proof entries for IV.7 (the hyperfine arc)\n')
w(block(['C-F1', 'C-F2', 'C-F3', 'C-F4', 'C-F5', 'C-F6', 'C-F7', 'C-F8']))
w('\n')
w(sp('### IV.8 '))
w('\n#### Reproduction table (what to run, what to expect)\n')
m = re.search(r'(?ms)^## G\. Reproduction table.*?(?=^---\n\n## H\.)', proofs); assert m
w(re.sub(r'^## G\. [^\n]*\n', '', m.group(0)).strip())
w('\n---\n')
w(sp('## V. The frontier'))
w('\n**Proofs for Part V:** none exist; these are open items. Nothing in this part is claimed.\n\n---\n')
w(sp('## VI. Provenance'))
w('\n')
w(sp('## VII. Index'))
w('\n')
w(open(os.path.join(repo, 'explore', 'unified_spine_tail.md'), encoding='utf-8').read().strip())
print('\n'.join(O))
