#!/usr/bin/env python3

import csv
import typing as t
from types.events import Event

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-e", "--events", type=click.File("r"), required=True)
def example(events: t.TextIO):
    """Temporary. Shows how to read a single CSV."""
    reader = csv.DictReader(events)
    for row in reader:
        event = Event.model_validate(row)
        print(event)
        break


if __name__ == "__main__":
    cli()
