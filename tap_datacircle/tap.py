"""Singer tap for the Datacircle API."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_datacircle.streams import ApisStream, PlansStream


class TapDatacircle(Tap):
    name = "tap-datacircle"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.datacircle.dev/v1",
            description="The Datacircle API base URL.",
        ),
    ).to_dict()

    def discover_streams(self):
        return [ApisStream(self), PlansStream(self)]


if __name__ == "__main__":
    TapDatacircle.cli()
