from fastapi import APIRouter
from api.endpoints import task_endpoints

api_router = APIRouter()
api_router.include_router(task_endpoints.router)