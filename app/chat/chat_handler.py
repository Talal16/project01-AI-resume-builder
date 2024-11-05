from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.chat.gpt_integration import generate_cv_text
from app.models.history_model import HistoryModel
from typing import Dict

router = APIRouter()

class CVSectionInput(BaseModel):
    user_id: int
    section: str  
    content: str
    job_description: str

class ChatResponse(BaseModel):
    section: str
    response: str

chat_memory: Dict[int, list] = {}

@router.post("/generate_cv_section", response_model=ChatResponse)
async def generate_cv_section(data: CVSectionInput):
   

    user_id = data.user_id
    section = data.section
    content = data.content
    job_description = data.job_description

    try:
        generated_text = generate_cv_text(content, job_description, section)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating CV section: {e}")

    if user_id not in chat_memory:
        chat_memory[user_id] = []
    chat_memory[user_id].append({"section": section, "response": generated_text})


    history_entry = HistoryModel(user_id=user_id, section=section, response=generated_text)
    await history_entry.save()

    return ChatResponse(section=section, response=generated_text)
