# DWD Pollen + School Holidays (Germany-specific)

Two independent `rest:` sensor examples for Germany-based users, both
hitting free, no-API-key-required open data endpoints.

> **Region-specific.** Both sensors need region/subdivision values swapped
> for your own location — the values shown are placeholders, not real
> region codes. This pattern won't produce meaningful data until you do.

## What it does

- **DWD grass pollen forecast**: polls DWD (Deutscher Wetterdienst /
  German Weather Service)'s open pollen-alert data
  (`opendata.dwd.de/climate_environment/health/alerts/s31fg.json`, DWD's
  own public endpoint) and extracts today's/tomorrow's grass-pollen level
  for a given region by matching `region_id`/`partregion_id` in the
  response. DWD publishes a region/subregion list — look up your own
  before relying on this (the `region_id: 1` / `partregion_id: -1` in the
  example are placeholders, not a real region).
- **School holidays**: polls `openholidaysapi.org` for upcoming school
  holidays in a German state (`subdivisionCode`, ISO 3166-2 style, e.g.
  `DE-BY` for Bavaria — the example — or your own state), producing a
  binary sensor for "is tomorrow a school holiday."

## Prerequisites

- None beyond core Home Assistant's `rest:` integration — both APIs are
  free and don't require a key.

## Customizing

- Replace the `region_id`/`partregion_id` pair with your own from DWD's
  published pollen-region reference.
- Replace `subdivisionCode=DE-BY` with your own German state's code (or a
  different `countryIsoCode` entirely if openholidaysapi.org supports your
  country).
- Both sensors poll every 6 hours (`scan_interval: 21600`) since neither
  data source updates more often than that.

## Full YAML

See [`rest_sensors.yaml`](rest_sensors.yaml).
