# ha-automation-cookbook

A grab-bag of independent, copy-pasteable Home Assistant automation
patterns. Each one solves its own problem and stands alone — this isn't one
cohesive system, just a collection of small, generalizable tricks found
useful enough to write up properly. Pick whichever pattern is relevant to
you; none of them depend on each other.

## Patterns

| Pattern | What it does | Notes |
|---|---|---|
| [`rpi-cooling-fan-hysteresis`](patterns/rpi-cooling-fan-hysteresis) | Hysteresis pair (two thresholds) to control a Raspberry Pi cooling fan without flapping | |
| [`low-battery-fleet-report`](patterns/low-battery-fleet-report) | Daily scan of every `device_class: battery` sensor, reports low/critical devices | |
| [`dashboard-view-rotator`](patterns/dashboard-view-rotator) | Randomized-interval `input_select` rotation to drive a dashboard view switcher | Display card not included |
| [`tv-volume-cap`](patterns/tv-volume-cap) | Parental/guest volume limiter for any media_player, with nightly reset | |
| [`tv-ambient-bias-lighting`](patterns/tv-ambient-bias-lighting) | Syncs an accent light to the TV turning on/off in the dark | |
| [`sun-exposed-windows-notification`](patterns/sun-exposed-windows-notification) | Notifies which windows are currently sun-exposed | Standalone version of a calc used in `ha-sun-blind-automation` |
| [`dwd-pollen-and-school-holidays`](patterns/dwd-pollen-and-school-holidays) | REST sensors for German pollen forecast + school holidays | Germany-specific |
| [`pollen-medication-reminder`](patterns/pollen-medication-reminder) | Evening reminder based on tomorrow's pollen forecast | Germany-specific (depends on the pattern above) |

## Using a pattern

Each `patterns/<name>/` folder is self-contained: a `README.md` explaining
it, and one YAML file with the full automation (and any supporting
sensors/helpers it needs). Copy what you need into your own
`automations.yaml`/`configuration.yaml`, adjust entity ids and any
placeholder values (notify targets, region codes, thresholds) to match your
own setup.

## Related

- [`sun-exposed-windows-notification`](patterns/sun-exposed-windows-notification)
  is a lightweight standalone cousin of
  [ha-sun-blind-automation](https://github.com/ftrauernicht/ha-sun-blind-automation)'s
  full sun-based blind-control system — start here if you just want the
  notification, graduate to the full repo if you want blinds that move
  themselves.
- [`dashboard-view-rotator`](patterns/dashboard-view-rotator)'s automation
  half is here; the Lovelace card side isn't included in any `ha-*`
  repo currently.

Part of the `ha-*` Home Assistant toolkit — see also
[ha-dashboard-recipes](https://github.com/ftrauernicht/ha-dashboard-recipes)
and [ha-sun-blind-automation](https://github.com/ftrauernicht/ha-sun-blind-automation).

## Contributing

All changes happen via Pull Request — direct pushes to `main` are blocked,
including for the maintainer. See [CONTRIBUTING.md](CONTRIBUTING.md) for how
to add a new pattern.

## License

[MIT](LICENSE).
