#!/usr/bin/env python3

import csv
import typing as t

import click

from models.events import Event
from models.hot_leads import HotLead


@click.group()
def cli():
    pass


@cli.command()
@click.option("-e", "--events", type=click.File("r"), required=True)
def test_events(events: t.TextIO):
    """Temporary. Shows how to read a single CSV."""
    reader = csv.DictReader(events)
    for row in reader:
        event = Event.model_validate(row)
        print(event)


@cli.command()
@click.option(
    "-h", "--hot-leads", type=click.File("r", encoding="utf-8-sig"), required=True
)
def test_hot_leads(hot_leads: t.TextIO):
    """Temporary. Shows how to read a single CSV."""
    reader = csv.DictReader(hot_leads)
    for row in reader:
        hot_lead = HotLead.model_validate(row)
        print(hot_lead)


RFS_ORG_ID = "942"


@cli.command()
@click.option("-e", "--events", type=click.File("r"), required=True)
def filter_events(events: t.TextIO):
    """Filter events."""
    reader = csv.DictReader(events)
    assert reader.fieldnames is not None
    with click.get_text_stream("stdout") as stdout:
        writer = csv.DictWriter(stdout, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            event = Event.model_validate(row)
            if event.organization_id == RFS_ORG_ID:
                writer.writerow(row)


if __name__ == "__main__":
    cli()
