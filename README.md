# Hackaton AI Google using `adk` Framework | 12-September 2025

A small sample of the idea I developed in the hackaton. (A hackaton adk self-creation system + self-explanation module [just text instead of voice])

## App
To run the project in your computer

```bash
uv snyc
make adk
```

# Self created readme :D

---

## Multi-Agent System Hackathon Project

## Overview

This project is a multi-agent system designed to demonstrate the power of collaborative AI agents for solving complex problems. It features an "Agent Orchestra" architecture, where a central orchestrator agent delegates tasks to specialized agents.

## Project Structure

The project is structured as follows:
src/
├── agents/
├── code_creator/
│ ├── agent.py
│ ├── model.py
├── project_explainer/
│ ├── agent.py
│ ├── tools.py
├── init.py
├── agent.py


*   `src/agents/`: Contains the code for all the agents.
*   `src/agents/agent.py`: Defines the root agent (orquestator).
*   `src/agents/code_creator/`: Contains the code for the `Code_Generator` agent.
    *   `agent.py`: Defines the `Code_Generator` agent.
    *   `model.py`: Defines the input schema for the `Code_Generator` agent (using Pydantic).
*   `src/agents/project_explainer/`: Contains the code for the `Explanation_Agent`.
    *   `agent.py`: Defines the `Explanation_Agent`.
    *   `tools.py`: Contains tools used by the `Explanation_Agent`.

## Agents

### 1. Orquestator Agent

*   **Name:** orquestator
*   **Description:** Agent to orchestrate all other agents.
*   **Instruction:** Get the user query & route the other agents.
*   **Responsibility:** The central agent that receives user requests and delegates tasks to other agents based on their expertise.

### 2. Code\_Generator Agent

*   **Name:** Code\_Generator
*   **Description:** Agent to create a hackathon Python project idea based on user input.
*   **Instruction:** Given a Plan Input for a hackaton, create a small custom programming idea that uses a multi-agentic Python system to replicate that idea. Output the main description of the project & key ideas and create code blocks for the proposed agents (maximum 5).
*   **Responsibility:** Generates Python code for multi-agent systems based on a provided project type and domain.

### 3. Explanation\_Agent

*   **Name:** Explanation\_Agent
*   **Description:** Agent to explain the project to the jury in an innovative way.
*   **Instruction:** Explain the current project code to the hackaton jury. Use provided tools to access code.
*   **Responsibility:** Explains the project's inner workings to a jury or audience in a clear and engaging manner.

## Usage

1.  **Define a Plan Input:** Create a `PlanInput` object specifying the `project_type` and `domain` for your desired multi-agent system.

2.  **Run the Orquestator Agent:** The `Orquestator` agent will route the input to the `Code_Generator` agent.

3.  **Generate Code:** The `Code_Generator` agent will generate Python code for the multi-agent system.

4.  **Explain the Project:** The `Explanation_Agent` can be used to provide a clear explanation of the generated code.

## Example

```python
from agents.code_creator.model import PlanInput
from agents.agent import root_agent # Orquestrator agent

# Define a Plan Input
plan_input = PlanInput(project_type="educational games", domain="math")

# The next steps would involve calling the orquestrator with the plan_input
# and then executing the generated code. This is a simplified example.
```
