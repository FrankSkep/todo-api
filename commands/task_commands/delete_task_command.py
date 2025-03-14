from commands.command import Command
from repositories.task_repository import TaskRepository

class DeleteTaskCommand(Command):
    def __init__(self, task_repository: TaskRepository, task_id: int):
        self.task_repository = task_repository
        self.task_id = task_id

    def execute(self):
        return self.task_repository.delete_task(self.task_id)