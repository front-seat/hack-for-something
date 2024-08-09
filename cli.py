#!/usr/bin/env python3

import csv
import typing as t

import click

from generate_invite import generate_invite
from generate_matches import generate_matches
from models.events import Event
from models.hot_leads import HotLead


@click.group()
def cli():
    pass


FRIENDLY_DATE_FORMAT = "%A %m/%d"


@cli.command()
@click.option("-e", "--events", type=click.File("r"), required=True)
@click.option(
    "-h", "--hot-leads", type=click.File("r", encoding="utf-8-sig"), required=True
)
def test_matches(events: t.TextIO, hot_leads: t.TextIO):
    event_objs = [Event.model_validate(row) for row in csv.DictReader(events)]
    hot_lead_objs = [HotLead.model_validate(row) for row in csv.DictReader(hot_leads)]
    selected_event_ids = generate_matches(event_objs, hot_lead_objs[0])
    selected_events = [event for event in event_objs if event.id in selected_event_ids]
    invite_text = generate_invite(selected_events, hot_lead_objs[0])
    print(invite_text)
    print("\n")
    for i, selected_event in enumerate(selected_events):
        print(
            f"[{i+1}] {selected_event.title} on {selected_event.start_date.strftime(FRIENDLY_DATE_FORMAT)} {selected_event.browser_url}"
        )


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
