from fastapi import FastAPI, File, UploadFile, HTTPException, Header, Depends
from stt_model import transcribe
import os

app = FastAPI(
    title="Speech-to-Text API",
    description="API for transcribing audio files using Groq's Whisper model",
    version="1.0.0"
)

# Get API key from environment variable or use a default for development
API_KEY = os.getenv("API_KEY", "MY_SUPER_SECRET")

async def verify_api_key(x_api_key: str | None = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    return x_api_key

@app.post("/transcribe")
async def transcribe_endpoint(
    file: UploadFile = File(...),
    api_key: str = Depends(verify_api_key)
):
    """
    Transcribe an audio file to text.
    
    Args:
        file (UploadFile): The audio file to transcribe (WAV or MP3)
        api_key (str): API key for authentication
        
    Returns:
        dict: Contains the transcribed text
    """
    if file.content_type not in ("audio/wav", "audio/mpeg", "audio/x-wav"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a WAV or MP3 file"
        )
    
    try:
        audio_bytes = await file.read()
        text = transcribe(audio_bytes)
        return {"transcript": text}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        ) 