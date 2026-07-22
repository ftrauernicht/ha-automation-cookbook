# Contributing

Thanks for wanting to add or improve a pattern!

## Ground rules

- All changes land via Pull Request. Direct pushes to `main` are blocked for
  everyone, including the maintainer.
- Keep PRs focused: one pattern per PR, in general.
- The automated `Validate examples` check must pass before a PR can be
  merged.

## Adding a new pattern

1. Create a new folder under `patterns/<your-pattern-slug>/`.
2. Add a `README.md` explaining what it does, prerequisites, and any
   customization points.
3. Add one YAML file with the full, working example.
4. If your pattern only makes sense in a specific country/region, say so
   clearly at the top of the README (see `dwd-pollen-and-school-holidays`
   for an example of how this is flagged).
5. Use generic, clearly-marked placeholder values for anything
   personal/location-specific: notify targets (`notify.mobile_app_example`),
   region/subdivision codes, entity ids. Add a comment pointing out what the
   reader needs to replace.
6. Validate locally before opening the PR:
   ```bash
   pip install pyyaml jinja2
   python scripts/validate_examples.py
   ```
7. Open a Pull Request. The PR template has a checklist — fill it in.

## Improving an existing pattern

Same process — branch, edit, validate, PR. Keep the change scoped to the
one pattern you're touching.
