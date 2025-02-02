from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    done: bool

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: int

    class Config:
        orm_mode = True

class Task(TaskInDBBase):
    pass

class TaskInDB(TaskInDBBase):
    pass