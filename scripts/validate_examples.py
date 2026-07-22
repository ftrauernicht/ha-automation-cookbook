#!/usr/bin/env python3
"""Validate every pattern's YAML is parseable and every embedded Jinja
template is at least syntactically valid. Also checks that every
patterns/<slug>/ folder has both a README.md and at least one YAML file.

This is a lint, not a full Home Assistant config check: it does not render
templates or validate HA-specific schemas/filters, since installing full
Home Assistant in CI would be disproportionate for a docs/examples repo.
"""
import sys
from pathlib import Path

import yaml
from jinja2 import Environment

ROOT = Path(__file__).resolve().parent.parent
PATTERNS_DIR = ROOT / "patterns"


class HALoader(yaml.SafeLoader):
    """yaml.safe_load chokes on Home Assistant's custom YAML tags
    (!secret, !include, etc.) since they aren't part of standard YAML.
    Register permissive passthrough constructors so example files using
    them still parse for structural/Jinja validation purposes.
    """


def _passthrough(loader, node):
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    return None


for tag in ("!secret", "!include", "!include_dir_list", "!include_dir_named", "!input"):
    HALoader.add_constructor(tag, _passthrough)


def find_jinja_strings(value, path=""):
    if isinstance(value, str):
        if "{{" in value or "{%" in value:
            yield path, value
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from find_jinja_strings(v, f"{path}.{k}" if path else str(k))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from find_jinja_strings(v, f"{path}[{i}]")


def main():
    errors = []
    jinja_env = Environment()

    yaml_files = sorted(PATTERNS_DIR.rglob("*.yaml")) + sorted(PATTERNS_DIR.rglob("*.yml"))

    for path in yaml_files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        try:
            data = yaml.load(text, Loader=HALoader)
        except yaml.YAMLError as e:
            errors.append(f"{rel}: YAML parse error: {e}")
            continue

        for tpl_path, tpl_string in find_jinja_strings(data):
            try:
                jinja_env.parse(tpl_string)
            except Exception as e:
                errors.append(f"{rel}: Jinja syntax error at {tpl_path}: {e}")

    # Structural completeness: every patterns/<slug>/ needs a README + >=1 YAML file.
    if PATTERNS_DIR.is_dir():
        for slug_dir in sorted(p for p in PATTERNS_DIR.iterdir() if p.is_dir()):
            has_readme = (slug_dir / "README.md").is_file()
            has_yaml = any(slug_dir.glob("*.yaml")) or any(slug_dir.glob("*.yml"))
            if not has_readme:
                errors.append(f"patterns/{slug_dir.name}: missing README.md")
            if not has_yaml:
                errors.append(f"patterns/{slug_dir.name}: missing a .yaml/.yml file")

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    pattern_count = len([p for p in PATTERNS_DIR.iterdir() if p.is_dir()]) if PATTERNS_DIR.is_dir() else 0
    print(f"OK: {len(yaml_files)} files validated across {pattern_count} patterns")


if __name__ == "__main__":
    main()
