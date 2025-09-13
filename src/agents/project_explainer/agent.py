from google.adk.agents import Agent

from .tools import get_src_code


agent = Agent(

   name="Explanation_Agent",
   model="gemini-2.0-flash", 
   description="Agent to explain the project to the jury in an innovative way.",
   instruction="Explain the current project code to the hackaton jury. To access code use get_src_code tool by yourself.",
   tools=[get_src_code]
)
