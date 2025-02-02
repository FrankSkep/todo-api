from fastapi import FastAPI
from api.routers import api_router
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")