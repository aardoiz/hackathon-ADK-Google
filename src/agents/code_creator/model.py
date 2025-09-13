from pydantic import BaseModel


class PlanInput(BaseModel):
    project_type: str
    domain: str
