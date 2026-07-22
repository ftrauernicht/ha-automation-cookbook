# Dashboard View Rotator

A small trick for cycling a dashboard between two or more "views" (e.g. an
energy chart and a couple of camera feeds) without a perfectly mechanical
rhythm — the interval is randomized between 30 and 50 seconds each cycle,
via `{{ range(30, 51) | random }}` inside the trigger's `for:` duration.

## What it does

- An `input_select` helper holds the "current view" (any set of option
  strings you want — `energy`, `camera1`, `camera2` are just examples).
- A self-retriggering automation waits a random 30-50 seconds in the
  helper's *current* state, then advances it to the next option
  (`input_select.select_next`, which wraps back to the first option after
  the last one).
- Because the `for:` duration is re-evaluated as a fresh random value each
  time the automation triggers, the rotation never falls into an obvious
  fixed cadence.

## Display side (not included here)

This pattern only drives the `input_select` — pairing it with a Lovelace
card is up to you. Any card that can key off an `input_select`'s state
works: a `conditional` card, a `custom:state-switch` card (if you're using
HACS), or your own dashboard automation. The point of documenting it
separately is that the rotation logic is display-agnostic and reusable no
matter which card technology you pick.

## Customizing

- Add/remove/reorder `input_select` options to rotate through as many views
  as you want.
- Adjust the `range(30, 51)` bounds to change how fast or slow the rotation
  feels.
- Swap `input_select.select_next` for `input_select.select_option` with a
  computed value if you want non-sequential (e.g. weighted random) rotation
  instead of a simple cycle.

## Full YAML

See [`automation.yaml`](automation.yaml).
