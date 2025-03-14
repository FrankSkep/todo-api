from commands.command import Command
from repositories.task_repository import TaskRepository

class DeleteAllTasksCommand(Command):
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self):
        return self.task_repository.delete_all_tasks()