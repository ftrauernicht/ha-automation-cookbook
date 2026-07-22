# Sun-Exposed Windows Notification

Tells you which windows/facades are currently getting direct sun, without
automating any blinds — just the insight, as a notification, for anyone who
wants it without adopting a full blind-control system.

## What it does

- Any `cover` (or other entity) gets a custom `azimuth` attribute via
  `customize:` — the compass direction (0-359°) that window/facade faces.
  Entities without this attribute are simply not considered; there's no
  hardcoded list to maintain.
- When it's hot outside (adjust the threshold to taste), the automation
  computes the angular difference between the sun's current azimuth
  (`state_attr('sun.sun', 'azimuth')`) and each tracked entity's azimuth,
  wrapping the difference into a 0-180° range and treating anything within
  90° as "the sun is roughly hitting that facade."
- If anything qualifies, sends one notification listing all of them by
  name.

## Prerequisites

- A temperature sensor (`sensor.outside_temperature` in the example — swap
  for your own outdoor temp sensor).
- A `notify.mobile_app_*` target — replace the placeholder
  `notify.mobile_app_example`.

## Related

This is a deliberately lightweight, standalone cousin of the full
[`hassio-sun-blind-automation`](https://github.com/ftrauernicht/hassio-sun-blind-automation)
repo, which reuses this same azimuth-diff calculation but goes further:
automatically closing/reopening blinds, tracking manual overrides, and
per-cover target positions. Start here if you just want the notification;
graduate to the full system if you want the blinds to move themselves.

## Customizing

- The `90` (degrees either side of directly facing the sun) and `24`
  (temperature threshold) values are both easy dials to turn.
- Add as many `azimuth`-tagged entities as you have windows/facades.

## Full YAML

See [`automation.yaml`](automation.yaml).
