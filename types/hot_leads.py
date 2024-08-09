from datetime import date
from typing import Optional

import pydantic as p


class Candidate(p.BaseModel, frozen=True):
    RFSID: str
    full_name: str
    first_name: str
    last_name: str
    endorsement_office_locale: str
    general_election_year: int
    website: Optional[str] = None
    twitter: Optional[str] = None
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    primary_date: Optional[date] = None
    primary_election_year: Optional[int] = None
    general_date: Optional[date] = None
    runoff_election: Optional[bool] = None
    runoff_election_year: Optional[int] = None
    BIPOC: Optional[bool] = None
    office_name: str
    endorsement_office_level: str
    endorsement_district: Optional[str] = None
    endorsement_district_name: Optional[str] = None
    endorsement_campaign_facebook_url: Optional[str] = None
    endorsement_campaign_twitter_url: Optional[str] = None
    endorsement_campaign_url: Optional[str] = None
    district_population: Optional[int] = None
    pronouns: Optional[str] = None
    city: str
    zip_code: str
    bio_with_edits: Optional[str] = None
    state: str


# Example usage:
_candidate = Candidate(
    RFSID="12345",
    full_name="John Doe",
    first_name="John",
    last_name="Doe",
    endorsement_office_locale="City",
    general_election_year=2024,
    office_name="Mayor",
    endorsement_office_level="Local",
    city="Springfield",
    zip_code="12345",
    state="IL",
)
