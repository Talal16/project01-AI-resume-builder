
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base 


class ChatHistory(Base):
    __tablename__ = 'chat_history'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="chat_history")
    message = Column(String, nullable=False)
    response = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<ChatHistory(user_id={self.user_id}, message={self.message[:20]})>"

class PDFHistory(Base):
    __tablename__ = 'pdf_history'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pdf_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PDFHistory(user_id={self.user_id}, pdf_url={self.pdf_url})>"
