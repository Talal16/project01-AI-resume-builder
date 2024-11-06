from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.chat.chat_integration_service import ChatIntegrationService

router = APIRouter()
chat_service = ChatIntegrationService()

@router.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = await chat_service.handle_message(data)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")
