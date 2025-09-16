from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.blog import CreateBlog, DisplayedBlog, UpdateBlog
from db.session import get_db
from db.controllers.blog import create_new_blog, get_blog_by_id, get_all_blogs, update_blog_by_id


router = APIRouter()

@router.post("/", response_model=DisplayedBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog

@router.get("/{id}", response_model=DisplayedBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = get_blog_by_id(id=id, db=db)
    if not blog:
        return HTTPException(detail=f"Blog with id: {id}, does not exist", status_code=status.HTTP_404)
    return blog

@router.get("", response_model=list[DisplayedBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = get_all_blogs(db=db)
    return blogs

@router.put("/", response_model=DisplayedBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session):
    blog = update_blog_by_id(id=id, blog=blog, db=db)
    if not blog:
        raise HTTPException(f"Blog with id: {id}, does not exist", status_code=status.HTTP_404)
    return blog