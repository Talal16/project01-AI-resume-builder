# services/user_service.py

from sqlalchemy.orm import Session
from app.models.user_model import User

def update_user_profile(db_session: Session, user_id: int, full_name: str = None, skills: str = None):
    # Retrieve the user by user_id
    user = db_session.query(User).filter(User.id == user_id).first()
    
    # If user is not found, return None
    if not user:
        return None
    
    # Update user details
    if full_name is not None:
        user.full_name = full_name
    if skills is not None:
        user.skills = skills
    
    # Commit changes to the database
    db_session.commit()
    db_session.refresh(user)  # Refresh to get the updated user details
    
    return user
