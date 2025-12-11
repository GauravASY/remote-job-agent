from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv
load_dotenv()
from agent import career_assistant



async def main():
    result = await Runner.run(career_assistant, "What are tips for landing a job at Google with one year of experience?")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
