from datetime import datetime
from pydantic import BaseModel, model_validator, ConfigDict


class CreateBlog(BaseModel):
    title: str
    slug: str = ""
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


class DisplayedBlog(BaseModel):
    title: str
    content: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # (v2) replaces orm_mode=True