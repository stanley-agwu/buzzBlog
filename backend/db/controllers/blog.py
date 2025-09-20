from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db:Session, author_id: int = 1):
    blog = Blog(
        title = blog.title,
        slug = blog.slug,
        content = blog.content,
        author_id = author_id,
        )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_blog_by_id(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def get_all_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs

def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return None
    blog_in_db.title = blog.title if blog.title else blog_in_db.title
    blog_in_db.content = blog.content if blog.content else blog_in_db.content
    db.add(blog_in_db)
    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db

def delete_blog_by_id(id: int, db: Session, author_id: int):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return { "error": f"Could not find blog with id: {id}" }
    blog_in_db.delete()
    db.commit()
    return { "msg": f"Success, deleted blog with id: {id}" }