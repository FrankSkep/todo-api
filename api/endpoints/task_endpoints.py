from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from repositories.task_repository import TaskRepository
from schemas.task_schema import Task, TaskCreate, TaskUpdate
from commands.task_commands.create_task_command import CreateTaskCommand
from commands.task_commands.update_task_command import UpdateTaskCommand
from commands.task_commands.delete_task_command import DeleteTaskCommand
from commands.task_commands.get_tasks_command import GetTasksCommand
from commands.task_commands.get_task_command import GetTaskCommand
from commands.task_commands.delete_all_tasks_command import DeleteAllTasksCommand
from commands.task_commands.get_done_tasks_command import GetDoneTasksCommand

# router with prefix "/tasks" and tag "tasks"
router = APIRouter(prefix="/tasks", tags=["tasks"])

# Dependency to get the task repository
def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)

# Endpoint to create a task
@router.post('', response_model=Task)
def create_task(task: TaskCreate, task_repository: TaskRepository = Depends(get_task_repository)):
    command = CreateTaskCommand(task_repository, task)
    return command.execute()

# Endpoint to get all tasks
@router.get('', response_model=list[Task])
def get_tasks(task_repository: TaskRepository = Depends(get_task_repository)):
    command = GetTasksCommand(task_repository)
    return command.execute()

# Endpoint to get a task by ID
@router.get('/{task_id}', response_model=Task)
def get_task(task_id: int, task_repository: TaskRepository = Depends(get_task_repository)):
    command = GetTaskCommand(task_repository, task_id)
    task = command.execute()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Endpoint to update a task by ID
@router.put('/{task_id}', response_model=Task)
def update_task(task_id: int, task: TaskUpdate, task_repository: TaskRepository = Depends(get_task_repository)):
    command = UpdateTaskCommand(task_repository, task_id, task)
    return command.execute()

# Endpoint to delete a task by ID
@router.delete('/{task_id}', response_model=Task)
def delete_task(task_id: int, task_repository: TaskRepository = Depends(get_task_repository)):
    command = DeleteTaskCommand(task_repository, task_id)
    return command.execute()

# Endpoint to delete all tasks
@router.delete('', response_model=list[Task])
def delete_all_tasks(task_repository: TaskRepository = Depends(get_task_repository)):
    command = DeleteAllTasksCommand(task_repository)
    return command.execute()

# Endpoint to get all completed tasks
@router.get('/done/', response_model=list[Task])
def get_done_tasks(task_repository: TaskRepository = Depends(get_task_repository)):
    command = GetDoneTasksCommand(task_repository)
    return command.execute()