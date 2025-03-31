from pydantic import BaseModel, Field

class Sign_in(BaseModel):
    name: str
    group: str

class Student(Sign_in):
    id: int
    score: int
    
    class Config:
        from_attributes = True
