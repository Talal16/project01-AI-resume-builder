# routers/degrees.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from app.middleware.authenticate_user import authenticate_user
from app.database import get_db
from app.services.degree_service import add_degree, update_degree
from app.models.user_model import Degrees

# Define router
router = APIRouter()

# Pydantic model for adding a new degree
class DegreeCreate(BaseModel):
    degree_name: str = Field(..., example="Bachelor of Science")
    institution: str = Field(..., example="University of XYZ")
    graduation_year: int = Field(..., example=2022)

# Pydantic model for updating an existing degree
class DegreeUpdate(BaseModel):
    degree_name: str = None
    institution: str = None
    graduation_year: int = None

@router.post("/degrees", response_model=dict)
async def add_degree_endpoint(
    degree_data: DegreeCreate,
    user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    # Add the degree to the user profile
    new_degree = add_degree(
        db_session=db,
        user_id=user.id,
        degree_name=degree_data.degree_name,
        institution=degree_data.institution,
        graduation_year=degree_data.graduation_year
    )
    
    return {
        "degree_id": new_degree.id,
        "degree_name": new_degree.degree_name,
        "institution": new_degree.institution,
        "graduation_year": new_degree.graduation_year
    }

@router.put("/degrees/{degree_id}", response_model=dict)
async def update_degree_endpoint(
    degree_id: int,
    degree_data: DegreeUpdate,
    user=Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    # Check if the degree belongs to the authenticated user
    degree = db.query(Degrees).filter(Degrees.id == degree_id, Degrees.user_id == user.id).first()
    if not degree:
        raise HTTPException(status_code=404, detail="Degree not found or does not belong to the user")

    # Update the degree details
    updated_degree = update_degree(
        db_session=db,
        degree_id=degree_id,
        degree_name=degree_data.degree_name,
        institution=degree_data.institution,
        graduation_year=degree_data.graduation_year
    )
    
    if not updated_degree:
        raise HTTPException(status_code=404, detail="Degree update failed")
    
    return {
        "degree_id": updated_degree.id,
        "degree_name": updated_degree.degree_name,
        "institution": updated_degree.institution,
        "graduation_year": updated_degree.graduation_year
    }
