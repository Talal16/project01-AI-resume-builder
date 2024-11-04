from sqlalchemy.orm import Session
from app.models.user_model import User
from app.auth.auth_handler import verify_password, create_access_token
from fastapi import HTTPException, status
from datetime import timedelta

def authenticate_user(db: Session, username: str, password: str):
    #check username and password
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None

def login_user(db: Session, username: str, password: str):
    #return an access token 
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}
