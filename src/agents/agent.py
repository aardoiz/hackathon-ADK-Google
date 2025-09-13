from google.adk.agents import Agent

from .code_creator.agent import agent as code_creator
from .project_explainer.agent import agent as project_explainer


root_agent = Agent(

   name="orquestator",
   model="gemini-2.0-flash", 
   description="Agent to orquestrate all other agents.",
   instruction="Get the user query & route the other agents",
   sub_agents=[code_creator, project_explainer],
)
