
from fastapi import FastAPI

from app.models.base import Base
from app.models.user_model import User  
from app.models.history_model import ChatHistory, PDFHistory  
from app.database import engine  # Ensure `engine` is defined and connected


# Database configuration


# Create tables
Base.metadata.create_all(bind=engine)


# FastAPI
app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI CV Maker API!"}
