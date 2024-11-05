
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base 



# Update User model to include relationship with Degrees
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    full_name = Column(String, nullable=True)
    linkedin_profile = Column(String, nullable=True)
    skills = Column(String, nullable=True)

    # Establishing a relationship with Degrees
    # degrees = relationship("Degrees", back_populates="user") 

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, full_name={self.full_name})>"

class Degrees(Base):
    __tablename__ = 'degrees'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to link with users
    degree_name = Column(String, nullable=False)  # Name of the degree (e.g., Bachelor of Science)
    institution = Column(String, nullable=False)  # Institution name (e.g., University of XYZ)
    graduation_year = Column(Integer, nullable=False)  # Year of graduation (e.g., 2020)
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for record creation

    user = relationship("User", back_populates="degrees")  # Link back to User model

    def __repr__(self):
        return f"<Degree(degree_name={self.degree_name}, institution={self.institution}, year={self.graduation_year})>"
