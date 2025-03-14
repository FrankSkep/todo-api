from commands.command import Command
from schemas.task_schema import TaskUpdate
from repositories.task_repository import TaskRepository

class UpdateTaskCommand(Command):
    def __init__(self, task_repository: TaskRepository, task_id: int, task: TaskUpdate):
        self.task_repository = task_repository
        self.task_id = task_id
        self.task = task

    def execute(self):
        return self.task_repository.update_task(self.task_id, self.task)