import datetime

import pydantic as p

EVENT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f %Z"


# def parse_dt(v: str | datetime.datetime) -> datetime.datetime | None:
#     """Parse datetiumes in the CSV format."""
#     if isinstance(v, datetime.datetime):
#         return v
#     if not v:
#         return None
#     return datetime.datetime.strptime(v, EVENT_DATETIME_FORMAT)


# def serialize_dt(v: datetime.date | None) -> str | None:
#     """Serialize datetimes."""
#     return v.strftime(EVENT_DATETIME_FORMAT) if v else None


# type OptionalEventDateTime = t.Annotated[
#     datetime.date | None,
#     p.PlainSerializer(serialize_dt),
#     p.BeforeValidator(parse_dt),
# ]


class Event(p.BaseModel, frozen=True):
    id: str
    title: str
    summary: str | None = None
    description: str | None = None
    featured_image_url: str | None = None
    # is_high_priority: bool = False TODO
    organization_id: str
    organization__name: str
    organization__slug: str
    organization__is_coordinated: bool
    organization__is_independent: bool
    organization__race_type: str
    organization__is_primary_campaign: bool
    organization__state: str
    organization__district: str | None = None
    organization__candidate_name: str | None = None
    # utc_organization__modified_date: OptionalEventDateTime = None
    location__is_private: bool = False
    location__venue: str | None = None
    location__address_line_1: str | None = None
    location__address_line_2: str | None = None
    location__locality: str | None = None
    location__region: str | None = None
    location__country: str | None = None
    location__postal_code: str | None = None
    # location__lat: float | None = None
    # location__lon: float | None = None
    # utc_location__modified_date: OptionalEventDateTime = None
    location__congressional_district: str | None = None
    location__state_leg_district: str | None = None
    location__state_senate_district: str | None = None
    event_timezone: str
    event_type: str
    browser_url: str | None = None
    # utc_created_date: datetime.datetime
    # utc_modified_date: datetime.datetime
    # utc_deleted_date: OptionalEventDateTime = None
    visibility: str
    is_created_by_volunteer_host: bool = False
    registration_mode: str
    van_name: str | None = None
    contact__name: str | None = None
    contact__email_address: str | None = None
    contact__phone_number: str | None = None
    approval_status: str
    rejection_message: str | None = None
    referrer__utm_source: str | None = None
    referrer__utm_medium: str | None = None
    referrer__utm_campaign: str | None = None
    referrer__utm_term: str | None = None
    referrer__utm_content: str | None = None
    referrer__url: str | None = None
    owner_id: str | None = None
    # utc_owner__modified_date: OptionalEventDateTime = None
    owner__given_name: str | None = None
    owner__family_name: str | None = None
    owner__email_address: str | None = None
    owner__phone_number: str | None = None
    owner__postal_code: str | None = None
    creator_id: str | None = None
    # utc_creator__modified_date: OptionalEventDateTime = None
    creator__given_name: str | None = None
    creator__family_name: str | None = None
    creator__email_address: str | None = None
    creator__phone_number: str | None = None
    creator__postal_code: str | None = None
    # utc_reviewed_date: OptionalEventDateTime = None
    reviewed_by_id: str | None = None
    # utc_reviewed_by__modified_date: OptionalEventDateTime = None
    reviewed_by__given_name: str | None = None
    reviewed_by__family_name: str | None = None
    reviewed_by__email_address: str | None = None
    reviewed_by__phone_number: str | None = None
    reviewed_by__postal_code: str | None = None
    accessibility_notes: str | None = None
    accessibility_status: str | None = None
    is_virtual: bool = False
    virtual_action_url: str | None = None
    event_campaign_id: str | None = None
    event_campaign__slug: str | None = None
    source_schema: str
    source_table: str
    vendor: str
    segment_by_key: str | None = None
    vendor_unique_event_id: str
    data_owner_id: str
    data_owner_code: str
    start_date: datetime.date = p.Field(alias="utc_start_date_iso")


# Example usage:
_event = Event(
    id="12345",
    title="Campaign Rally",
    organization_id="org123",
    organization__name="Example Org",
    organization__slug="example-org",
    organization__is_coordinated=True,
    organization__is_independent=False,
    organization__race_type="General",
    organization__is_primary_campaign=False,
    organization__state="CA",
    event_timezone="America/Los_Angeles",
    event_type="Rally",
    utc_created_date=datetime.datetime.now(datetime.UTC),
    utc_modified_date=datetime.datetime.now(datetime.UTC),
    visibility="Public",
    registration_mode="Open",
    approval_status="Approved",
    source_schema="public",
    source_table="events",
    vendor="ExampleVendor",
    vendor_unique_event_id="vendor_12345",
    data_owner_id="owner123",
    data_owner_code="OWN123",
    utc_start_date_iso=datetime.date(2022, 1, 1),
)
