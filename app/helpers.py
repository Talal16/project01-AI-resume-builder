from sqlalchemy.orm import Session
from models import User, Degrees, ChatHistory
from datetime import datetime

def load_user_data(db_session: Session, user_id: int) -> str:
    # Retrieve user data from the database
    user = db_session.query(User).filter(User.id == user_id).first()
    degrees = db_session.query(Degrees).filter(Degrees.user_id == user_id).all()

    if user:
        # Compile user data into a string format for the assistant
        user_data = {
            "full_name": user.full_name,
            "linkedin_profile": user.linkedin_profile,
            "skills": user.skills,
            "degrees": [{"degree_name": degree.degree_name, "institution": degree.institution, "graduation_year": degree.graduation_year} for degree in degrees]
        }
        initial_message = (
            f"User Details:\n"
            f"Name: {user_data['full_name']}\n"
            f"LinkedIn: {user_data['linkedin_profile']}\n"
            f"Skills: {user_data['skills']}\n"
            f"Degrees:\n" +
            "\n".join([f"- {degree['degree_name']} from {degree['institution']} ({degree['graduation_year']})" for degree in user_data["degrees"]])
        )
        return initial_message
    return "User details not found."

def save_chat_history(db_session: Session, user_id: int, user_message: str, assistant_reply: str):
    # Save each message-response pair in the chat history
    chat_history = ChatHistory(
        user_id=user_id,
        message=user_message,
        response=assistant_reply,
        timestamp=datetime.utcnow()
    )
    db_session.add(chat_history)
    db_session.commit()
