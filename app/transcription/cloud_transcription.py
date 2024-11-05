import os
from google.cloud import speech
from google.oauth2 import service_account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Set the path to the Google Cloud service account key

def transcribe_audio(file_path: str) -> str:
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    print("cloud trans01")
    client = speech.SpeechClient(credentials=credentials)

    # Read the audio file
    with open(file_path, "rb") as audio_file:
        print(file_path)
        audio_content = audio_file.read()

    # Configure audio and request settings
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Use MP3 encoding
        sample_rate_hertz=16000,  # Change according to your audio file's sample rate
        language_code="en-US",
    )

    # Send the audio file to Google Cloud Speech-to-Text API
    response = client.recognize(config=config, audio=audio)

    # Extract the transcribed text
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript
