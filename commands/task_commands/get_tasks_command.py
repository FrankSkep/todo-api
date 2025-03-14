from commands.command import Command
from repositories.task_repository import TaskRepository

class GetTasksCommand(Command):
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self):
        return self.task_repository.get_tasks()