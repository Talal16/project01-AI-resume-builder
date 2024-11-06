# router.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.chat.chat_integration_service import ChatIntegrationService
from app.middleware.authenticate_user import authenticate_user
from app.database import get_db

router = APIRouter()

@router.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket, db: Session = Depends(get_db), user=Depends(authenticate_user)):
    await websocket.accept()
    chat_service = ChatIntegrationService(db_session=db, user_id=user.id)
    
    try:
        while True:
            # Receive user input
            user_message = await websocket.receive_text()
            
            # Pass the message to ChatIntegrationService to handle conversation context
            response = await chat_service.handle_message(user_message)
            
            # Send back the assistant's response
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")
