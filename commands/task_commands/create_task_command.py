from commands.command import Command
from schemas.task_schema import TaskCreate
from repositories.task_repository import TaskRepository

class CreateTaskCommand(Command):
    def __init__(self, task_repository: TaskRepository, task: TaskCreate):
        self.task_repository = task_repository
        self.task = task

    def execute(self):
        return self.task_repository.create_task(self.task)