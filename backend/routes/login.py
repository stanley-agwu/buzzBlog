from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from core.hasher import Hasher
from db.controllers.login import get_user
from core.security import create_access_token

router = APIRouter()

def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.password):
        return False
    return user

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(detail="Incorrect username or password", status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token(data={ "sub": user.username })
    return { "access_token": access_token, "token_type": "bearer" }