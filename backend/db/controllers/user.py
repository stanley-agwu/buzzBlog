from sqlalchemy.orm import Session
from schemas.user import User as UserSchema
from db.models.user import User
from core.hasher import Hasher

def create_new_user(user: UserSchema, db:Session):
    user = User(
        username = user.username,
        password = Hasher.get_password_hash(user.password),
        is_collab_user = False,
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user