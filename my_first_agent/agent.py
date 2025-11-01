# Location: my_first_agent/agent.py

from google.adk.agents import LlmAgent

# The ADK runtime looks for an object named `root_agent`
# The agent will automatically find the API key in the environment.
root_agent = LlmAgent(
    name="assistant_agent",
    model="gemini-2.5-flash",
    # DO NOT add api_key=... here
    description="A helpful and creative assistant for a wide range of tasks.",
    instruction="""
You are a friendly and knowledgeable assistant named Magic.
Your goal is to help users with their questions clearly and concisely.
When asked for creative tasks, like writing a poem or a joke, be imaginative!
"""
)