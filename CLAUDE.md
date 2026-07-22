# CLAUDE.md

Guidance for Claude Code (or any AI coding agent) working in this repository.

## What this repo is

An independent grab-bag of Home Assistant automation patterns — each
`patterns/<slug>/` folder is its own self-contained example, not part of one
larger system. There is no build step and no shared runtime between
patterns. A typical PR touches exactly one pattern folder (either adding a
new one, or fixing/extending an existing one) — it should be unusual for a
single PR to touch multiple pattern folders at once.

## Hard rules

- **Never commit directly to `main`.** Always work on a branch and open a
  Pull Request. Branch protection enforces this for everyone including the
  repo owner.
- Every `patterns/<slug>/` folder must contain both a `README.md` and at
  least one `.yaml`/`.yml` file — a PR that adds one without the other
  should be rejected. `scripts/validate_examples.py` enforces this
  automatically in CI.
- Entity ids, notify targets, region/subdivision codes, and any other
  location-specific values in examples must stay generic and clearly marked
  as placeholders (e.g. `notify.mobile_app_example` with a "replace with
  your own" comment) — never imitate a real personal setup, even when
  contributing a new pattern.
- Region-specific patterns (currently `dwd-pollen-and-school-holidays` and
  `pollen-medication-reminder`, both Germany-specific) must say so clearly
  at the top of their README.
- English only, in all docs and YAML comments.

## Repo layout

- `patterns/<slug>/README.md` + one YAML file — the actual content, one
  self-contained pattern per folder.
- `scripts/validate_examples.py` — YAML/Jinja-syntax validation plus a
  structural check that every pattern folder has both a README and a YAML
  file; run locally and in CI.
- `.github/workflows/validate.yml` — CI job (`Validate examples`) required
  by branch protection before merge.
