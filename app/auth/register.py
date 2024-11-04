from sqlalchemy.orm import Session
from app.models.user_model import User
from app.auth.auth_handler import get_password_hash
from fastapi import HTTPException, status

def register_user(db: Session, username: str, email: str, password: str):
    # Check if the user exists
    if db.query(User).filter(User.username == username).first() or db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered")
    
    # Create a new user with hashed password
    new_user = User(
        username=username,
        email=email,
        password_hash=get_password_hash(password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
