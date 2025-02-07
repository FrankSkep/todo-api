from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.task_service import TaskService
from repositories.task_repository import TaskRepository
from schemas.task_schema import Task, TaskCreate, TaskUpdate

router = APIRouter()

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    task_repository = TaskRepository(db)
    return TaskService(task_repository)

@router.post('/tasks', response_model=Task)
def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)

@router.get('/tasks', response_model=list[Task])
def get_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.get_tasks()

@router.get('/tasks/{task_id}', response_model=Task)
def get_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put('/tasks/{task_id}', response_model=Task)
def update_task(task_id: int, task: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
    return task_service.update_task(task_id, task)

@router.delete('/tasks/{task_id}', response_model=Task)
def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    return task_service.delete_task(task_id)

@router.delete('/tasks', response_model=list[Task])
def delete_all_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.delete_all_tasks()

@router.get('/tasks/done/', response_model=list[Task])
def get_done_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.get_done_tasks()