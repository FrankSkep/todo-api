from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import TaskCreate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_task(self, task: TaskCreate):
        db_task = Task(**task.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def get_tasks(self):
        return self.db.query(Task).all()
    
    def get_task(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()
    
    def update_task(self, task_id: int, task: Task):
        task_to_update = self.get_task(task_id)
        task_to_update.title = task.title
        task_to_update.description = task.description
        task_to_update.done = task.done
        self.db.commit()
        return task_to_update
    
    def delete_task(self, task_id: int):
        task_to_delete = self.get_task(task_id)
        self.db.delete(task_to_delete)
        self.db.commit()
        return task_to_delete
    
    def delete_all_tasks(self):
        tasks = self.get_tasks()
        for task in tasks:
            self.db.delete(task)
        self.db.commit()
        return tasks
    
    def get_done_tasks(self):
        return self.db.query(Task).filter(Task.done == True).all()