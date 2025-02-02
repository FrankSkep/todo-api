from repositories.task_repository import TaskRepository
from models.task_model import Task

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository
    
    def get_tasks(self):
        return self.task_repository.get_tasks()
    
    def get_task(self, task_id: int):
        return self.task_repository.get_task(task_id)
    
    def create_task(self, task: Task):
        return self.task_repository.create_task(task)
    
    def update_task(self, task_id: int, task: Task):
        return self.task_repository.update_task(task_id, task)
    
    def delete_task(self, task_id: int):
        return self.task_repository.delete_task(task_id)
    
    def delete_all_tasks(self):
        return self.task_repository.delete_all_tasks()
    
    def get_done_tasks(self):
        return self.task_repository.get_done_tasks()