from fastapi import APIRouter
from routes import user
from routes import blog
from routes import login

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(blog.router, prefix="/blogs", tags=["blogs"])
api_router.include_router(login.router, prefix="/login", tags=["login"])