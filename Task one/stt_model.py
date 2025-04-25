import os
from groq import Groq

# Initialize the Groq client once at startup
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe(audio_bytes: bytes) -> str:
    """
    Transcribe audio bytes using Groq's Whisper model.
    
    Args:
        audio_bytes (bytes): The audio file content in bytes
        
    Returns:
        str: The transcribed text
    """
    try:
        # Create a temporary file to store the audio
        temp_path = "temp_audio.mp3"
        with open(temp_path, "wb") as f:
            f.write(audio_bytes)
            
        # Create transcription using Groq's Whisper
        with open(temp_path, "rb") as file:
            response = client.audio.transcriptions.create(
                file=(temp_path, file.read()),
                model="whisper-large-v3",
                response_format="text"  # Get plain text output
            )
            
        # Clean up the temporary file
        os.remove(temp_path)
        
        return response
        
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}") 