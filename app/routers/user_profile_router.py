# routers/user_profile.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.middleware.authenticate_user import authenticate_user
from app.database import get_db
from app.services.user_service import update_user_profile
from models import User

# Define router
router = APIRouter()

# Define Pydantic model for updating user profile
class UserProfileUpdate(BaseModel):
    full_name: str = None
    skills: str = None

@router.get("/profile", response_model=dict)
async def get_user_profile(user: User = Depends(authenticate_user), db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.id == user.id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return user profile details
    return {
        "username": user_data.username,
        "email": user_data.email,
        "full_name": user_data.full_name,
        "linkedin_profile": user_data.linkedin_profile,
        "skills": user_data.skills
    }

@router.put("/profile", response_model=dict)
async def update_user_profile_endpoint(
    user_profile_update: UserProfileUpdate,
    user: User = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    # Update user profile details
    updated_user = update_user_profile(
        db_session=db,
        user_id=user.id,
        full_name=user_profile_update.full_name,
        skills=user_profile_update.skills
    )
    
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return the updated profile details
    return {
        "username": updated_user.username,
        "email": updated_user.email,
        "full_name": updated_user.full_name,
        "linkedin_profile": updated_user.linkedin_profile,
        "skills": updated_user.skills
    }
