# Pollen Medication Reminder

Reminds you the night before if tomorrow's pollen forecast is bad enough
that you might want to take an allergy medication in advance.

## What it does

- Built on top of the `sensor.grass_pollen_tomorrow` sensor from the
  [`dwd-pollen-and-school-holidays`](../dwd-pollen-and-school-holidays)
  pattern.
- DWD reports pollen load as one of 7 text tiers, low to high:
  `0`, `0-1`, `1`, `1-2`, `2`, `2-3`, `3`. The automation looks up tomorrow's
  tier's position in that list and compares it against a configurable
  index (default: tier `1-2` and above counts as "medium-to-high").
- If the threshold is met, sends one reminder notification in the evening.

## Prerequisites

- The `dwd-pollen-and-school-holidays` pattern's grass-pollen sensor (or
  any sensor reporting the same DWD tier strings).
- A `notify.mobile_app_*` target — replace the placeholder
  `notify.mobile_app_example`.

## Customizing

- `medium_index`: raise it to only get reminded on genuinely high-load
  days, or lower it to get reminded earlier/more often.
- Swap the grass-pollen sensor for a different DWD pollen type (tree,
  ragweed, etc.) if that's what affects you.
- Replace the generic "take your allergy medication" message with whatever
  specific reminder text you want.

## Full YAML

See [`automation.yaml`](automation.yaml).
