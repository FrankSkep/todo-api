from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

class Task(TaskBase):
    id: int
    completed: bool
    user_id: int

    class Config:
        from_attributes = True