from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
import os
from prompt import career_assistant_prompt


google_model = LitellmModel(
    model="gemini/gemini-2.5-flash",  # specific LiteLLM model identifier
    api_key=os.environ.get("GEMINI_API_KEY")
)

career_assistant = Agent(
    name= "Gaurav",
    instructions= career_assistant_prompt,
    model = google_model
)
