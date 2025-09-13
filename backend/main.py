from fastapi import FastAPI, HTTPException, Depends
from core.config import settings
from routes.base import api_router

def include_router(app: FastAPI):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()

@app.get("/")
async def root():
    return {"message": "Hello World"}