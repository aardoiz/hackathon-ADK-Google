from google.adk.agents import Agent

from src.agents.code_creator.agent import a


agent = Agent(

   name="orquestator",
   model="gemini-2.0-flash-exp", 
   description="Agent to orquestrate all other agents.",
   instruction="Route the other agents",
   sub_agents=[voice_creator, deep_creator, project_explainer, enhancer],
)
