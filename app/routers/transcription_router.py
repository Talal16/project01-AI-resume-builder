from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.transcription.whisper_api import transcribe_audio

import os
from app.middleware.authenticate_user import authenticate_user
router = APIRouter()


@router.post("/transcribe-audio", dependencies=[Depends(authenticate_user)])
async def transcribe_audio_route(file: UploadFile = File(...)):
   
    file_path = f"temp_{file.filename}"
    try:
        # Save the uploaded file temporarily
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Call the transcription function
        transcription_text = transcribe_audio(file_path)
        return {"transcription": transcription_text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Cleanup file
        if os.path.exists(file_path):
            os.remove(file_path)
