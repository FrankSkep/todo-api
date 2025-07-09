from fastapi import APIRouter
from api.endpoints import task_endpoints, auth_endpoints

api_router = APIRouter()
api_router.include_router(auth_endpoints.router)
api_router.include_router(task_endpoints.router)