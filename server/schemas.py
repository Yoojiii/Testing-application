from pydantic import BaseModel, Field

class Registration(BaseModel):
    name: str
    group: str = Field(max_length=10)

