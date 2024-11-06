
from sqlalchemy.orm import Session
from models.user_model import Degrees

def add_degree(db_session: Session, user_id: int, degree_name: str, institution: str, graduation_year: int):
    new_degree = Degrees(
        user_id=user_id,
        degree_name=degree_name,
        institution=institution,
        graduation_year=graduation_year
    )
    db_session.add(new_degree)
    db_session.commit()
    db_session.refresh(new_degree)
    return new_degree

def update_degree(db_session: Session, degree_id: int, degree_name: str = None, institution: str = None, graduation_year: int = None):
    degree = db_session.query(Degrees).filter(Degrees.id == degree_id).first()
    
    if not degree:
        return None
    
    if degree_name is not None:
        degree.degree_name = degree_name
    if institution is not None:
        degree.institution = institution
    if graduation_year is not None:
        degree.graduation_year = graduation_year
    
    db_session.commit()
    db_session.refresh(degree)
    return degree
