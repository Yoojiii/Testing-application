from pydantic import BaseModel, Field

class Sign_in(BaseModel):
    name: str
    group: str = Field(max_length=10)
    isAdmin: bool = False

class user(Sign_in):
    score: int
