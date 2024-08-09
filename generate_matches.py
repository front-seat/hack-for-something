import os

import dotenv
import openai

import models
import models.events
import models.hot_leads

dotenv.load_dotenv()
# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.chat.completions.create

prompt_template = """
Please pick the top {n} events out of the events listed below that would be appropriate for the specified at the end of this message:
[START EVENTS LIST]
{event_list}
[END EVENTS LIST]
The candidate has the following bio: {candidate_bio} 
The candidate lives in: {candidate_state}

Please return only a list of event IDs seperated by semicolons.
"""


def generate_matches(
    events: list[models.events.Event], candidate: models.hot_leads.HotLead
):
    prompt = prompt_template.format(
        n=5,
        event_list=events,
        candidate_bio=candidate.bio_with_edits,
        candidate_state=candidate.state,
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # This is the model used by ChatGPT
        messages=[
            {
                "role": "system",
                "content": "You are helping an organizer suggest events for a potential candidate for office. Choose 3. Order them from best possible match (most relevant, nearest, soon, etc.) to least.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.split(";")
