# Alpha ratio search, Codex replay

Author/client: Codex in ChatGPT Work Mode. No independent review claimed. Prior candidate files retain their existing authorship.

Target supplied by user: 1/137.036, anywhere within or between scales. No physical identification is required for reporting a numerical candidate. Search does not prove a coupling law.

Read QUESTION.md, README.md, CLAUDE.md, maps/alpha_candidates.md and existing raw outputs. Deep reference inspected: Maths 6/explore/alpha_explore.py and alpha_photon.py. Their running-scale claims were not adopted or independently verified.

New calculation: 60-digit mpmath evaluation of 14,641 expressions (a/b)*(phi/2)^n, with eleven named floor quantities and n=-60..60. Full definitions are in the script. Zero inverse ratios round to 137.036 at three decimal places. Closest new inverse ratio is 136.835272871786598140555225033828079047234312562827384014736. This finite grammar does not exhaust recursive structure.

A previous grammar search found the closer numerical candidate

R = 7 ln(phi)/(375 acos(1/3))
  = 0.00729725172731605365518193627584598131420389015270223679979388.

Its reciprocal is 137.037892807872526483783380570704389179383816714745931072105. Relative reciprocal error against 137.036 is 0.000013812486299413904254214737035444550219042549008516536566215. The factor 375/7 was selected by the prior target-directed rational grammar, not forced by a demonstrated mechanism. This is a near-miss, not an alpha derivation. All printed digits are numerical evaluations at finite precision, not exact decimal identities.

Append-only qualification of maps/alpha_candidates.md: its sentence concluding that alpha is not in any single level is unsupported by the finite searches. Nor does being algebraic prevent agreement with a finite-precision measured value. What those searches establish is failure within their tested expressions and operators only. Do not inherit the stronger exclusion.

Replay:
`py -3 -I -u explore/alpha_ratio_replay_codex.py`

Here py.exe was inaccessible. Successful equivalent:
`& 'C:\Users\Dad\AppData\Local\Python\bin\python.exe' -I -u explore/alpha_ratio_replay_codex.py`

Raw accepted and failed candidate values: explore/alpha_ratio_replay_codex.out. Source/input hashes are printed there, including immutable inherited Maths 5/6 floor hashes from floor/PROVENANCE.md. Script and output are new files; floor and previous evidence untouched.

Operational failure: creating Codex/alpha-ratio-search branch failed because .git refs are not writable in this session. No commit or push performed. Initial branch main; pre-existing changes left intact. apply_patch could not write the new path; native PowerShell Set-Content succeeded. The first Python launcher attempt failed before numerical execution.
