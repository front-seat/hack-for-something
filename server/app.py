import csv
import pathlib

from litestar import Litestar, get
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Template
from litestar.template.config import TemplateConfig

from models.events import Event
from models.hot_leads import HotLead

TEMPLATES_DIR = (pathlib.Path(__file__).parent / "templates").resolve()
template_config = TemplateConfig(engine=JinjaTemplateEngine, directory=TEMPLATES_DIR)

# Load data at startup time, because this is a hack.
EVENTS_CSV = pathlib.Path(__file__).parent.parent / "data" / "small-events.csv"
HOT_LEADS_CSV = pathlib.Path(__file__).parent.parent / "data" / "hot-leads.csv"

EVENTS = []

with open(EVENTS_CSV) as f:
    reader = csv.DictReader(f)
    EVENTS = [Event.model_validate(row) for row in reader]

with open(HOT_LEADS_CSV, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    HOT_LEADS = [HotLead.model_validate(row) for row in reader]


@get("/")
async def index() -> Template:
    return Template("index.html", context={"events": EVENTS, "hot_leads": HOT_LEADS})


app = Litestar(template_config=template_config, route_handlers=[index])
