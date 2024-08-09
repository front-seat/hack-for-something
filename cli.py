#!/usr/bin/env python3

import csv
import json
import typing as t

import click
import pydantic as p


class Event(p.BaseModel):
    """A single event in mobilize.us."""

    id: int
    title: str


class Candidate(p.BaseModel):
    """A hot list candidate for RFS."""

    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option("-e", "--events", type=click.File("r"), required=True)
def example(events: t.TextIO):
    """Temporary. Shows how to read a single CSV."""
    reader = csv.DictReader(events)
    for row in reader:
        print(json.dumps(row, indent=2))


if __name__ == "__main__":
    cli()
