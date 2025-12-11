from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel
import os


google_model = LitellmModel(
    model="gemini/gemini-2.5-flash",  # specific LiteLLM model identifier
    api_key=os.environ.get("GEMINI_API_KEY")
)

career_assistant = Agent(
    name= "Carrey the career assistant",
    instructions= "You are an expert career advisor with over a decade of experience helping people find their dream jobs.",
    model = google_model
)
