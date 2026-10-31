# Builds lab/spine_lab.html from lab/spine_lab_src.html: embeds the rungs and their energy columns (maps/size_vs_energy_filled.csv, with provenance flags)
# and the M5 spine nodes (floor/M5_SPINE_10-9-26.md, parsed as written). Nothing is typed in by hand except three extra rungs marked below.
# Run: py -3 -I -X utf8 -u explore/build_lab.py
import csv, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
rows = list(csv.reader(open(os.path.join(ROOT, 'maps', 'size_vs_energy_filled.csv'), encoding='utf-8')))
h = rows[0]; n = (len(h) - 1)//2
cols = h[1:1 + n]; pcols = h[1 + n:]
ix = {c: i + 1 for i, c in enumerate(cols)}
want = [('hbar c / R (eV)', 'ħc/R'), ('Confinement kinetic (hbar c/R)^2 / 2 m (eV)', 'confinement kinetic'), ('Rest energy m c^2 (eV)', 'rest m c²'), ('Gravity G m m2 / R (eV)', 'gravity'),
        ('EM  alpha Q1Q2 hbar c / R (eV); Q1Q2 = 1 if neutral', 'EM'), ('Strong  C_F alpha_s hbar c / R (eV)', 'strong'), ('Weak, log10 eV (no underflow)', 'weak (log10)'),
        ('Binding / dissociation / cohesion total (eV)', 'binding'), ('First excitation (eV)', 'first excitation'), ('Spin / fine / isospin splitting (eV)', 'spin / fine'),
        ('Collective mode: vibration, phonon, octupole (eV)', 'collective'), ('Rotational (eV)', 'rotational'), ('Ambient kT, 298.15 K (eV)', 'kT 298 K'), ('CMB kT, 2.7255 K (eV)', 'kT CMB')]
def cls(nm):
    if nm.startswith(('tau', 'muon', 'electron')): return 'lepton'
    if nm.startswith('nucleon'): return 'hadron'
    if nm.startswith('12C nucleus'): return 'nuclear'
    if nm.startswith(('CO', 'C2')): return 'molecule'
    if nm.startswith('diamond'): return 'lattice'
    if nm.startswith('the gram'): return 'bulk'
    return 'atomic'
rungs = []
for r in rows[1:]:
    E = []
    for c, lab in want:
        v = r[ix[c]]; p = r[len(cols) + 1 + (ix[c] - 1)]
        E.append([lab, float(v), p])
    rungs.append(dict(name=r[0], R=float(r[ix['Size R (m)']]), cls=cls(r[0]), E=E))
rungs.append(dict(name='Planck length (anchor)', R=1.616255e-35, cls='anchor', E=[], note='The anchor assumption of the lab: the edge at tower copy k = 0 (spine nodes 17/18/33; non-discriminating).'))
rungs.append(dict(name='proton Compton length', R=2.1030891e-16, cls='hadron', E=[], note='hbar / (m_p c); r_p / this = 3.9977 (CODATA 2022).'))
rungs.append(dict(name='Hubble radius c/H0 (recalled, ±8%)', R=4.4e26, cls='cosmic', E=[], note='Order of magnitude only; recalled, not a saved source.'))
spine = []
raw = open(os.path.join(ROOT, 'floor', 'M5_SPINE_10-9-26.md'), 'rb').read()
text = raw.decode('utf-16') if (raw[0] in (255, 254)) else raw.decode('utf-8')
for line in text.splitlines():
    m = re.match(r'\|\s*\*\*([0-9A-Za-z/]+)\*\*\s*\|(.*)\|\s*$', line)
    if not m: continue
    parts = [p.strip() for p in m.group(2).split('|')]
    if len(parts) < 3: continue
    clean = lambda s: re.sub(r'\*\*|`', '', s)
    nid = m.group(1)
    spine.append(dict(id=nid, ids=nid.split('/') if '/' in nid else None, claim=clean(parts[0]), proof=clean(parts[1]), grade=clean(parts[2])))
for nd in spine:
    if nd['ids'] is None: del nd['ids']
src = open(os.path.join(ROOT, 'lab', 'spine_lab_src.html'), encoding='utf-8').read()
out = src.replace('/*DATA*/null', json.dumps(dict(rungs=rungs, spine=spine), ensure_ascii=False))
open(os.path.join(ROOT, 'lab', 'spine_lab.html'), 'w', encoding='utf-8').write(out)
print('rungs', len(rungs), 'spine nodes', len(spine), 'bytes', len(out))
