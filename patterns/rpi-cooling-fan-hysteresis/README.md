# RPi Cooling Fan Hysteresis

Keeps a Raspberry Pi's cooling fan from flapping on/off by using two different
thresholds instead of one: turn on above a high temperature, turn off below a
*lower* one. Right at a single boundary temperature, a fan controlled by only
one threshold will click on and off repeatedly as the reading jitters by
tenths of a degree around that value — hysteresis (a gap between the two
thresholds) fixes that.

## What it does

- A `command_line:` sensor reads `/sys/class/thermal/thermal_zone0/temp`
  directly (the Pi's CPU thermal zone, reported in millidegrees C) — no
  extra integration needed, works on any Pi running the HA Core container.
- **Turn on** above 65°C.
- **Turn off** below 50°C.
- Between 50°C and 65°C, the fan just stays in whatever state it was already
  in — that's the point.

## Prerequisites

- A `switch` entity controlling your fan (GPIO relay, smart plug, whatever
  you're using).
- Home Assistant running directly on the Pi whose temperature you want to
  read (or adjust the `command_line:` sensor's `command:` if reading a
  different host's thermal zone via SSH).

## Customizing

- Adjust the 65°C / 50°C thresholds to your hardware's comfort range — the
  only rule is "off" threshold must stay below "on" threshold, or you're
  back to flapping.
- Multiple thermal zones: `thermal_zone0` is usually the CPU package on a Pi,
  but check `ls /sys/class/thermal/` on your device if it doesn't match.

## Full YAML

See [`automation.yaml`](automation.yaml).
