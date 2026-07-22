# TV Ambient Bias Lighting

Turns on a dim accent/bias light behind the TV when it's on and it's dark,
and turns it back off the moment either condition stops being true.

## What it does

- Three named triggers (`tv_on`, `tv_off`, `became_light`) feed into one
  `choose:` action block, so all the "when should the light change" logic
  lives in one automation instead of being split across several.
- **TV turns on AND it's currently dark** (checked via a `sun` condition
  spanning sunset→sunrise): after a short debounce delay, sets the bias
  light to a dim warm-white preset.
- **TV turns off, OR it becomes light outside** (sunrise trigger) — either
  one turns the bias light back off, via an `or` condition group so either
  trigger source reaches the same action.
- The named trigger IDs (`id: "tv_on"` etc.) are what make the `choose:`
  block able to tell which of the three triggers actually fired, via
  `condition: trigger / id: "..."` checks.

## Prerequisites

- A `media_player` entity for the TV (any player exposing `on`/`off` state
  works).
- A `light` entity for the bias/accent lighting (a smart bulb or LED strip
  behind/near the TV).

## Customizing

- Swap `brightness_pct`/`color_name` for whichever preset/scene you like —
  or replace the `light.turn_on` call with `scene.turn_on` targeting a
  pre-built scene instead of inline attributes.
- Replace the `sun` before/after condition with a lux sensor threshold if
  you want brightness-based rather than sun-position-based darkness
  detection.
- Adjust the debounce `delay:` (2 seconds here) to taste.

## Full YAML

See [`automation.yaml`](automation.yaml).
