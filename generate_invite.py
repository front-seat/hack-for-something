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
Write a personalized invitation.
You are inviting {candidate_name} who is running for {candidate_office}.
Their bio is: {candidate_bio}
You are inviting them to {event_name} which is an {event_type} event.
The event description is: {event_description}
Please make your message friendly and engaging; personalize the content for this person, particularly focusing on any relevant issues they may be interested in."""


def generate_invitation(
    event: models.events.Event, candidate: models.hot_leads.HotLead
):
    prompt = prompt_template.format(
        candidate_name=candidate.full_name,
        candidate_office=candidate.office_name,
        candidate_bio=candidate.bio_with_edits,
        event_name=event.title,
        event_type=event.event_type,
        event_description=event.description,
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # This is the model used by ChatGPT
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that writes personalized invitations.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


# Example usage

invitation = generate_invitation(models.events._event, models.hot_leads._hot_lead)
print(invitation)
