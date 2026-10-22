#!/usr/bin/env python3
"""Render a task prompt locally with explicitly supplied variables (no I/O except files)."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

TOKEN = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

def render(template: str, values: dict[str, str]) -> str:
    missing = sorted(set(TOKEN.findall(template)) - set(values))
    if missing:
        raise ValueError("Fehlende Promptwerte: " + ", ".join(missing))
    extra = sorted(set(values) - set(TOKEN.findall(template)))
    if extra:
        raise ValueError("Nicht verwendete Promptwerte: " + ", ".join(extra))
    if any(not isinstance(v, str) or not v.strip() for v in values.values()):
        raise ValueError("Leere oder nichttextuelle Promptwerte sind nicht erlaubt")
    out = TOKEN.sub(lambda match: values[match.group(1)], template)
    if TOKEN.search(out):
        raise ValueError("Unaufgelöste Platzhalter im erzeugten Text")
    return out

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('template', type=Path)
    parser.add_argument('values', type=Path, help='JSON object with explicit variable strings')
    args = parser.parse_args()
    values = json.loads(args.values.read_text(encoding='utf-8'))
    if not isinstance(values, dict): raise ValueError('values must be JSON object')
    print(render(args.template.read_text(encoding='utf-8'), values))

if __name__ == '__main__': main()
