import uvicorn
from fastapi import FastAPI
from database import engine, Base
from api.routers import api_router

def create_app():
    Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(api_router, prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8070)
