import openai
import dotenv
import os 

dotenv.load_dotenv()
# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.chat.completions.create

def generate_invitation(name, event_type, date, location):
    prompt = f"Write a personalized invitation for {name} to a {event_type} on {date} at {location}. Make it friendly and engaging."

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # This is the model used by ChatGPT
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes personalized invitations."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# Example usage
name = "Alice"
event_type = "birthday party"
date = "June 15th"
location = "Sunset Beach"

invitation = generate_invitation(name, event_type, date, location)
print(invitation)