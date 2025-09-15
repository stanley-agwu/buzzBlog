from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.blog import CreateBlog, DisplayedBlog
from db.session import get_db
from db.controllers.blog import create_new_blog, get_blog_by_id


router = APIRouter()

@router.post("/", response_model=DisplayedBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog

@router.get('/{id}', response_model=DisplayedBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = get_blog_by_id(id=id, db=db)
    if not blog:
        return HTTPException(detail=f"Blog with id: {id}, does not exist", status_code=status.HTTP_404)
    return blog