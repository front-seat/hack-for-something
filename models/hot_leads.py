import pydantic as p


class HotLead(p.BaseModel, frozen=True):
    RFSID: str
    full_name: str = p.Field(alias="Full Name")
    first_name: str = p.Field(alias="firstName")
    last_name: str = p.Field(alias="lastName")
    # endorsement_office_locale: str
    # general_election_year: int = p.Field(alias="General Election Year")
    # website: str | None = None
    # twitter: str | None = None
    # instagram: str | None = None
    # facebook: str | None = None
    # primary_date: datetime.date | None = None
    # primary_election_year: int | None = None
    # general_date: datetime.date | None = None
    # runoff_election: bool | None = None
    # runoff_election_year: int | None = None
    # BIPOC: bool | None = None
    office_name: str = p.Field(alias="Office Name")
    # endorsement_office_level: str
    # endorsement_district: str | None = None
    # endorsement_district_name: str | None = None
    # endorsement_campaign_facebook_url: str | None = None
    # endorsement_campaign_twitter_url: str | None = None
    # endorsement_campaign_url: str | None = None
    # district_population: int | None = None
    # pronouns: str | None = None
    # city: str
    # zip_code: str
    bio_with_edits: str | None = None
    state: str = p.Field(alias="State")


# Example usage:
_hot_lead = HotLead(
    **{
        "Full Name": "John Doe",
        "firstName": "John",
        "lastName": "Doe",
        "Office Name": "Mayor",
        "State": "IL",
    }
)
