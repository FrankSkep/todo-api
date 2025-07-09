from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: TaskCreate, user_id: int):
        db_task = Task(
            title=task.title,
            description=task.description,
            user_id=user_id
        )
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_tasks(self, user_id: int):
        return self.db.query(Task).filter(Task.user_id == user_id).all()

    def get_task(self, task_id: int, user_id: int):
        return self.db.query(Task).filter(
            Task.id == task_id, 
            Task.user_id == user_id
        ).first()

    def update_task(self, task_id: int, task: TaskUpdate, user_id: int):
        db_task = self.get_task(task_id, user_id)
        if db_task:
            if task.title is not None:
                db_task.title = task.title
            if task.description is not None:
                db_task.description = task.description
            if task.completed is not None:
                db_task.completed = task.completed
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete_task(self, task_id: int, user_id: int):
        db_task = self.get_task(task_id, user_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
        return db_task

    def delete_all_tasks(self, user_id: int):
        tasks = self.get_tasks(user_id)
        for task in tasks:
            self.db.delete(task)
        self.db.commit()
        return tasks

    def get_done_tasks(self, user_id: int):
        return self.db.query(Task).filter(
            Task.user_id == user_id, 
            Task.completed == True
        ).all()

    def get_pending_tasks(self, user_id: int):
        return self.db.query(Task).filter(
            Task.user_id == user_id, 
            Task.completed == False
        ).all()