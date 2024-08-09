from datetime import datetime
from typing import Optional

import pydantic as p


class Event(p.BaseModel, frozen=True):
    dbt_source_relation: str
    id: str
    title: str
    summary: Optional[str] = None
    description: Optional[str] = None
    featured_image_url: Optional[str] = None
    is_high_priority: bool = False
    organization_id: str
    organization__name: str
    organization__slug: str
    organization__is_coordinated: bool
    organization__is_independent: bool
    organization__race_type: str
    organization__is_primary_campaign: bool
    organization__state: str
    organization__district: Optional[str] = None
    organization__candidate_name: Optional[str] = None
    utc_organization__modified_date: Optional[datetime] = None
    location__is_private: bool = False
    location__venue: Optional[str] = None
    location__address_line_1: Optional[str] = None
    location__address_line_2: Optional[str] = None
    location__locality: Optional[str] = None
    location__region: Optional[str] = None
    location__country: Optional[str] = None
    location__postal_code: Optional[str] = None
    location__lat: Optional[float] = None
    location__lon: Optional[float] = None
    utc_location__modified_date: Optional[datetime] = None
    location__congressional_district: Optional[str] = None
    location__state_leg_district: Optional[str] = None
    location__state_senate_district: Optional[str] = None
    event_timezone: str
    event_type: str
    browser_url: Optional[str] = None
    utc_created_date: datetime
    utc_modified_date: datetime
    utc_deleted_date: Optional[datetime] = None
    visibility: str
    is_created_by_volunteer_host: bool = False
    registration_mode: str
    van_name: Optional[str] = None
    contact__name: Optional[str] = None
    contact__email_address: Optional[str] = None
    contact__phone_number: Optional[str] = None
    approval_status: str
    rejection_message: Optional[str] = None
    referrer__utm_source: Optional[str] = None
    referrer__utm_medium: Optional[str] = None
    referrer__utm_campaign: Optional[str] = None
    referrer__utm_term: Optional[str] = None
    referrer__utm_content: Optional[str] = None
    referrer__url: Optional[str] = None
    owner_id: Optional[str] = None
    utc_owner__modified_date: Optional[datetime] = None
    owner__given_name: Optional[str] = None
    owner__family_name: Optional[str] = None
    owner__email_address: Optional[str] = None
    owner__phone_number: Optional[str] = None
    owner__postal_code: Optional[str] = None
    creator_id: Optional[str] = None
    utc_creator__modified_date: Optional[datetime] = None
    creator__given_name: Optional[str] = None
    creator__family_name: Optional[str] = None
    creator__email_address: Optional[str] = None
    creator__phone_number: Optional[str] = None
    creator__postal_code: Optional[str] = None
    utc_reviewed_date: Optional[datetime] = None
    reviewed_by_id: Optional[str] = None
    utc_reviewed_by__modified_date: Optional[datetime] = None
    reviewed_by__given_name: Optional[str] = None
    reviewed_by__family_name: Optional[str] = None
    reviewed_by__email_address: Optional[str] = None
    reviewed_by__phone_number: Optional[str] = None
    reviewed_by__postal_code: Optional[str] = None
    accessibility_notes: Optional[str] = None
    accessibility_status: Optional[str] = None
    is_virtual: bool = False
    virtual_action_url: Optional[str] = None
    event_campaign_id: Optional[str] = None
    event_campaign__slug: Optional[str] = None
    source_schema: str
    source_table: str
    vendor: str
    segment_by_key: Optional[str] = None
    vendor_unique_event_id: str
    data_owner_id: str
    data_owner_code: str
    event_id: str


# Example usage:
_event = Event(
    dbt_source_relation="example_relation",
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
    utc_created_date=datetime.utcnow(),
    utc_modified_date=datetime.utcnow(),
    visibility="Public",
    registration_mode="Open",
    approval_status="Approved",
    source_schema="public",
    source_table="events",
    vendor="ExampleVendor",
    vendor_unique_event_id="vendor_12345",
    data_owner_id="owner123",
    data_owner_code="OWN123",
    event_id="event_12345",
)
