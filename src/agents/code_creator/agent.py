from google.adk.agents import Agent

from .model import PlanInput


template = """
agent = Agent(
   name="",
   model="gemini-2.0-flash", 
   description="",
   instruction="",
)
"""


agent = Agent(
   name="Code_Generator",
   model="gemini-2.0-flash", 
   description="Agent to create a hackaton python project idea based on user_input.",
   instruction=f"Given a Plan Input for a hackaton, create a small custom programming idea that uses a multi-agentic python system to replicate that idea. You must output the main description of the project & key ideas; and create code blocks for the agents proposed (maximum 5). Use this template for each agent (ADK framework) {template}",
   input_schema=PlanInput
)
