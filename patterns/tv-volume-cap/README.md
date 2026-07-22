# TV Volume Cap

A parental/guest-friendly volume limiter for any `media_player`: cap the
volume at a helper-controlled percentage, with a nightly reset so the cap
doesn't accidentally stay in effect forever.

## What it does

- `input_number.tv_volume_limit` holds the current cap (0-100%).
- **Enforce Limit**: whenever the TV's volume changes *or* the limit helper
  changes, re-clamp the volume back down to the limit if it's currently
  above it. A small epsilon tolerance (0.02) on the comparison stops the
  clamp's own `volume_set` call from immediately re-triggering the
  automation again — without it you'd get an infinite retrigger loop from
  floating-point rounding alone.
- **Nightly Reset**: sets the limit back to 100% (no cap) at midnight every
  day. Whoever wants the cap active just lowers the helper again — this
  avoids a cap set once, forgotten, and silently affecting everyone
  indefinitely.

## Prerequisites

- Any `media_player` entity that supports `volume_level` (most do).

## Customizing

- Change `media_player.living_room_tv` to your own player entity (or
  duplicate the automations per player if you want independent caps).
- Adjust the epsilon (`0.02`) if you see either false triggers or a cap
  that doesn't hold tightly enough — depends on how granular your player's
  volume steps are.
- Skip the nightly reset automation entirely if you want a cap that's
  meant to be permanent rather than a daily opt-in.

## Full YAML

See [`automation.yaml`](automation.yaml).
