from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from repositories.task_repository import TaskRepository
from schemas.task_schema import Task, TaskCreate, TaskUpdate
from schemas.user_schema import User
from api.endpoints.auth_endpoints import get_current_active_user

# router with prefix "/tasks" and tag "tasks"
router = APIRouter(prefix="/tasks", tags=["tasks"])

# Dependency to get the task repository
def get_task_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)

# Endpoint to create a task
@router.post('', response_model=Task)
def create_task(
    task: TaskCreate, 
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    return task_repository.create_task(task, current_user.id)

# Endpoint to get all tasks
@router.get('', response_model=list[Task])
def get_tasks(
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    return task_repository.get_tasks(current_user.id)

# Endpoint to get a task by ID
@router.get('/{task_id}', response_model=Task)
def get_task(
    task_id: int, 
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    task = task_repository.get_task(task_id, current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    return task

# Endpoint to update a task by ID
@router.put('/{task_id}', response_model=Task)
def update_task(
    task_id: int, 
    task: TaskUpdate, 
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    updated_task = task_repository.update_task(task_id, task, current_user.id)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    return updated_task

# Endpoint to delete a task by ID
@router.delete('/{task_id}', response_model=Task)
def delete_task(
    task_id: int, 
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    deleted_task = task_repository.delete_task(task_id, current_user.id)
    if not deleted_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Task not found"
        )
    return deleted_task

# Endpoint to delete all tasks
@router.delete('', response_model=list[Task])
def delete_all_tasks(
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    return task_repository.delete_all_tasks(current_user.id)

# Endpoint to get all completed tasks
@router.get('/completed/', response_model=list[Task])
def get_done_tasks(
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    return task_repository.get_done_tasks(current_user.id)

# Endpoint to get all pending tasks
@router.get('/pending/', response_model=list[Task])
def get_pending_tasks(
    task_repository: TaskRepository = Depends(get_task_repository),
    current_user: User = Depends(get_current_active_user)
):
    return task_repository.get_pending_tasks(current_user.id)