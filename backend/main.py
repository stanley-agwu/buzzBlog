from fastapi import FastAPI, HTTPException, Depends
from core.config import settings
# from db.session import engine
# from db.base import Base



# def create_tables():
#     Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # create_tables() -> creation of tables removed from start application. Should be by Alembic only.
    return app

app = start_application()

@app.get("/")
async def root():
    return {"message": "Hello World"}