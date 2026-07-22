# Low Battery Fleet Report

A single daily automation that scans **every** `sensor.*` entity in your
installation with `device_class: battery` and tells you which ones are
running low — no need to maintain a manual list of battery-powered devices
as your fleet of sensors/locks/remotes grows.

## What it does

- Runs once a day (10:00 by default).
- Discovers battery sensors dynamically via
  `states.sensor | selectattr('attributes.device_class', 'eq', 'battery')` —
  add a new battery-powered device to Home Assistant and it's automatically
  covered, no automation edit needed.
- Validates each sensor's state is a clean number via a regex match before
  using it — a sensor stuck on `unavailable` or `unknown` is silently
  skipped instead of crashing the whole report with a template error.
- Splits results into **warning** (below 20%) and **critical** (below 10%)
  tiers.
- Sends both a mobile notification and a `persistent_notification` (visible
  in the HA UI even if you miss the push notification).
- Only fires at all if there's actually something to report — no empty
  "everything's fine" spam every single day.

## Prerequisites

- At least one entity with `device_class: battery` (most battery-powered
  Zigbee/Z-Wave/Bluetooth devices expose this automatically).
- A `notify.mobile_app_*` target — the example uses a placeholder
  `notify.mobile_app_example`; replace it with your own.

## Customizing

- `warning_threshold` / `critical_threshold`: adjust the two cutoff
  percentages.
- `excluded_entities`: a list of entity_ids (or use a `reject` on a
  name-fragment match instead) for any device known to report its battery
  level unreliably — keeps it out of the report entirely rather than
  generating recurring false alarms.
- Trigger time: change `at: "10:00:00"` to whenever you want the daily scan.

## Full YAML

See [`automation.yaml`](automation.yaml).
