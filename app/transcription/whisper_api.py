import requests
import time

import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(file_path: str) -> str:
        
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
    params = {"return_timestamps": "true"}     
    with open(file_path, "rb") as f:
        data = f.read()
        for attempt in range(5):  # Retry up to 5 times
            response = requests.post(API_URL, headers=headers, data=data, params=params)
                
            if response.status_code == 200:
                result = response.json()
                return result.get("text", "Transcription failed.")
                
            elif response.status_code == 503:
                print("Model is loading, retrying...")
                time.sleep(5)  
            else:
                raise Exception(f"Failed to transcribe audio. Status code: {response.status_code}, Message: {response.text}")

    raise Exception("Exceeded maximum retry attempts for audio transcription.")