# Location: run_programmatically.py (in your root folder)

import asyncio
from dotenv import load_dotenv
import os

# 1. Load environment variables from .env file FIRST.
# This ensures os.environ["GOOGLE_API_KEY"] is set
# BEFORE we import the agent.
load_dotenv()

# 2. Check if the key was loaded, just to be safe.
if "GOOGLE_API_KEY" not in os.environ:
    print("‼️ FATAL ERROR: GOOGLE_API_KEY not found in environment.")
    print("Please ensure your .env file is in the root directory (adk-bootcamp-python) and has the key.")
    exit()

# 3. Now, import the agent. The agent.py file will read the key.
from my_first_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# 4. Match the APP_NAME to your agent's package name.
APP_NAME = "my_first_agent"

# Unique IDs for the user and the conversation session.
USER_ID = "user_12345"
SESSION_ID = "session_67890"


async def main():
    """The main function to run the agent programmatically."""
    runner = Runner(
        agent=root_agent,
        session_service=InMemorySessionService(),
        app_name=APP_NAME,
    )

    print(f"Creating session: {SESSION_ID}")
    await runner.session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    user_message = Content(parts=[Part(text="Write a haiku about dogs who love engineers.")])
    print(f"User Message: '{user_message.parts[0].text}'")

    print("\n--- Agent Response ---")
    final_response = ""

    try:
        async for event in runner.run_async(
            user_id=USER_ID, session_id=SESSION_ID, new_message=user_message
        ):
            if event.is_final_response() and event.content:
                final_response = event.content.parts[0].text.strip()
                print(final_response)
        print("--- End of Response ---\n")
    except Exception as e:
        print(f"\n‼️ An error occurred during agent execution: {e}\n")


# Run the asynchronous main function.
if __name__ == "__main__":
    asyncio.run(main())