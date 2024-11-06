# helpers.py

from sqlalchemy.orm import Session
from app.models.user_model import User, Degrees
from app.models.history_model import ChatHistory
from datetime import datetime

def load_user_data(db_session: Session, user_id: int) -> str:
    user = db_session.query(User).filter(User.id == user_id).first()
    degrees = db_session.query(Degrees).filter(Degrees.user_id == user_id).all()
    if user:
        user_data = (
            f"Name: {user.full_name}\n"
            f"LinkedIn: {user.linkedin_profile}\n"
            f"Skills: {user.skills}\n"
            f"Degrees:\n" +
            "\n".join([f"- {degree.degree_name} from {degree.institution} ({degree.graduation_year})" for degree in degrees])
        )
        return user_data
    return "User details not found."

def save_chat_history(db_session: Session, user_id: int, user_message: str, assistant_reply: str):
    chat_history = ChatHistory(
        user_id=user_id,
        message=user_message,
        response=assistant_reply,
        timestamp=datetime.utcnow()
    )
    db_session.add(chat_history)
    db_session.commit()
