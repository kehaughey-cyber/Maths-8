#!/usr/bin/env python3
"""Install the pre-commit hook that runs the guard on staged files. Git does not clone hooks, so run this once per clone:
    py -3 -I guard/install_hook.py
A blocked commit prints the file:line of each ERROR. Fix the text; do not bypass the hook."""
import os, pathlib, subprocess

root = pathlib.Path(__file__).resolve().parent.parent
hooks = pathlib.Path(subprocess.run(['git', 'rev-parse', '--git-path', 'hooks'], cwd=root, capture_output=True, text=True).stdout.strip())
hooks = hooks if hooks.is_absolute() else root / hooks
hook = hooks / 'pre-commit'
hook.write_text('#!/bin/sh\nexec py -3 -I guard/check.py --staged\n', newline='\n')
os.chmod(hook, 0o755)
print('installed', hook)
