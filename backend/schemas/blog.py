from datetime import date

from pydantic import BaseModel, model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str | None = None
    content: str | None = None

    @model_validator(mode="before")
    @classmethod
    def generate_slug(cls, values):
        # Runs before field validation; safe place to derive one field from another
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: str | None
    created_at: date

    class Config:
        orm_mode = True