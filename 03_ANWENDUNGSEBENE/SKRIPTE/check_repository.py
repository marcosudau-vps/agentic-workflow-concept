#!/usr/bin/env python3
"""Offline repository integrity / link / source hash / derivation checks."""
from __future__ import annotations
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
LINK=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
CODEFENCE=re.compile(r'^\s*```')

def markdown_targets(text: str) -> list[str]:
    # Skip fenced code to avoid reporting illustrative paths as links.
    out=[];fenced=False
    for line in text.splitlines():
        if CODEFENCE.match(line):fenced=not fenced;continue
        if fenced:continue
        out.extend(LINK.findall(line))
    return out

def check() -> list[str]:
    errors=[]
    for file in ROOT.rglob('*.json'):
        try: json.loads(file.read_text(encoding='utf-8'))
        except Exception as exc:errors.append(f'JSON error {file.relative_to(ROOT)}: {exc}')
    for file in ROOT.rglob('*.md'):
        if 'QUELLEN' in file.relative_to(ROOT).parts: continue  # archival excerpts need not resolve relative links
        text=file.read_text(encoding='utf-8')
        for link in markdown_targets(text):
            target=link.split('#',1)[0]
            if not target or target.startswith(('https:','http:','mailto:','{{','<')):continue
            target=target.split(' ',1)[0]
            dest=(file.parent/target).resolve()
            if not dest.is_relative_to(ROOT.resolve()):errors.append(f'Link leaves repo: {file.relative_to(ROOT)} -> {link}')
            elif not dest.exists():errors.append(f'Broken link: {file.relative_to(ROOT)} -> {link}')
    source_file=ROOT/'01_ARBEITSEBENE/07_QUELLENMANIFEST.json'
    if source_file.is_file():
        obj=json.loads(source_file.read_text(encoding='utf-8'))
        for source in obj.get('files',[]):
            p=ROOT/source['path']
            if not p.is_file():errors.append(f'Missing source: {source["path"]}')
            elif hashlib.sha256(p.read_bytes()).hexdigest()!=source['sha256']:
                errors.append(f'Changed immutable source: {source["path"]}')
    mapping=ROOT/'01_ARBEITSEBENE/06_ABLEITUNGSMATRIX.csv'
    if mapping.is_file():
        with mapping.open(encoding='utf-8',newline='') as fh:
            for row in csv.DictReader(fh):
                for key in ('concept','application'):
                    for item in filter(None,(row.get(key) or '').split(';')):
                        if not (ROOT/item.strip()).is_file():
                            errors.append(f'Missing mapping: {row.get("rule_id")} -> {item}')
    for file in (ROOT/'03_ANWENDUNGSEBENE/SKILLS').glob('*/SKILL.md'):
        if not file.read_text(encoding='utf-8').startswith('---\n'):
            errors.append(f'SKILL frontmatter missing: {file.relative_to(ROOT)}')
    return errors
if __name__=='__main__':
    issues=check()
    print(f'Validated {sum(1 for _ in ROOT.rglob("*.md"))} Markdown files and {sum(1 for _ in ROOT.rglob("*.json"))} JSON files')
    for issue in issues: print('ERROR',issue,file=sys.stderr)
    print('RESULT:', 'FAIL' if issues else 'PASS (only structure/provenance, not substantive acceptance)')
    sys.exit(bool(issues))
