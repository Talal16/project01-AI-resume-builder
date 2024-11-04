
from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.base import Base
from app.database import engine, SessionLocal, get_db 
from app.routers import auth_router 

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI CV Maker API!"}

# the auth router - login and reg
app.include_router(auth_router.router)
