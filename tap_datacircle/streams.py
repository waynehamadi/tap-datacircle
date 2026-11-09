"""Streams for the Datacircle API."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.pagination import BaseOffsetPaginator
from singer_sdk.streams import RESTStream


class PlansPaginator(BaseOffsetPaginator):
    def has_more(self, response) -> bool:
        return bool(response.json()["plans"])


class DatacircleStream(RESTStream):
    @property
    def url_base(self) -> str:
        return self.config["api_url"]


class ApisStream(DatacircleStream):
    name = "apis"
    path = "/apis"
    primary_keys = ("slug",)
    replication_key = None
    schema = th.PropertiesList(
        th.Property("api", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("plans", th.IntegerType),
        th.Property("providers", th.IntegerType),
        th.Property("sheetPage", th.StringType),
        th.Property("bestPage", th.StringType),
        th.Property("best", th.ObjectType(additional_properties=True)),
    ).to_dict()

    def parse_response(self, response):
        yield from response.json()


class PlansStream(DatacircleStream):
    name = "plans"
    path = "/plans"
    primary_keys = ("provider", "api", "plan")
    replication_key = None
    schema = th.PropertiesList(
        th.Property("provider", th.StringType),
        th.Property("api", th.StringType),
        th.Property("plan", th.StringType),
        th.Property("website", th.StringType),
        th.Property("pricingPage", th.StringType),
        th.Property("pitch", th.StringType),
        th.Property("score", th.NumberType),
        th.Property("perThousand", th.NumberType),
        th.Property("strengths", th.ArrayType(th.StringType)),
    ).to_dict()

    def get_new_paginator(self):
        return PlansPaginator(start_value=0, page_size=50)

    def get_url_params(self, context, next_page_token):
        return {"limit": 50, "offset": next_page_token or 0}

    def parse_response(self, response):
        yield from response.json()["plans"]

