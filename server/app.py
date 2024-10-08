import csv
import pathlib

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

from generate_invite import generate_invite
from generate_matches import generate_matches
from models.events import Event
from models.hot_leads import HotLead

TEMPLATES_DIR = (pathlib.Path(__file__).parent / "templates").resolve()
template_config = TemplateConfig(engine=JinjaTemplateEngine, directory=TEMPLATES_DIR)

# Load data at startup time, because this is a hack.
EVENTS_CSV = pathlib.Path(__file__).parent.parent / "data" / "small-events.csv"
HOT_LEADS_CSV = pathlib.Path(__file__).parent.parent / "data" / "hot-leads.csv"

EVENTS = []
HOT_LEADS = []

with open(EVENTS_CSV) as f:
    reader = csv.DictReader(f)
    EVENTS = [Event.model_validate(row) for row in reader]

with open(HOT_LEADS_CSV, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    unordered_leads = [HotLead.model_validate(row) for row in reader]
    for hot_lead in unordered_leads:
        if hot_lead.city == "Houston" and hot_lead.full_name != "Mo Jenkins":
            HOT_LEADS.append(hot_lead)
    for hot_lead in unordered_leads:
        if hot_lead.city != "Houston":
            HOT_LEADS.append(hot_lead)


@get("/")
async def index() -> Template:
    return Template("index.html", context={"events": EVENTS, "hot_leads": HOT_LEADS})


@get("/email/{hot_lead_full_name: str}")
async def email(hot_lead_full_name: str) -> Template:
    hot_lead = next(hl for hl in HOT_LEADS if hl.full_name == hot_lead_full_name)
    return Template("email.html", context={"hot_lead": hot_lead})


@get("/api/email/{hot_lead_full_name: str}")
async def email_api(hot_lead_full_name: str) -> dict[str, str]:
    hot_lead = next(hl for hl in HOT_LEADS if hl.full_name == hot_lead_full_name)
    selected_event_ids = generate_matches(EVENTS, hot_lead)
    selected_events = [event for event in EVENTS if event.id in selected_event_ids]
    invite_text = generate_invite(selected_events, hot_lead)
    invite_text = invite_text or "An error occurred while generating the invite."
    invite_text = invite_text.replace("```html", "").replace("```", "")
    return {"invite_text": invite_text}


app = Litestar(
    template_config=template_config, route_handlers=[index, email, email_api]
)
