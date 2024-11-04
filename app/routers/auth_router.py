from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.auth import register, login
from pydantic import BaseModel, EmailStr

router = APIRouter()

# Pydantic models for user registration and login
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    return register.register_user(db=db, username=user.username, email=user.email, password=user.password)

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    return login.login_user(db=db, username=user.username, password=user.password)
