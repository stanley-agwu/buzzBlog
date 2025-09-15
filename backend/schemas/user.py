from pydantic import BaseModel
from pydantic import Field

from pydantic import BaseModel, constr, field_validator


class User(BaseModel):
    username: constr(min_length=4)  # at least 4 characters
    password: constr(min_length=8)  # at least 8 characters

    @field_validator("password")
    @classmethod
    def password_strength(cls, value: str) -> str:
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(not char.isalnum() for char in value):
            raise ValueError("Password must contain at least one special character")
        return value


class DisplayedUser(BaseModel):
    id: int
    username: str
    is_collab_user: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        from_attributes = True