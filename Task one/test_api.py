import requests
import os
import sys

def test_transcription_api(api_url, api_key, audio_file_path):
    """
    Test the transcription API with a sample audio file.
    
    Args:
        api_url (str): The URL of the transcription API
        api_key (str): The API key for authentication
        audio_file_path (str): Path to the audio file to transcribe
    """
    print(f"Testing transcription API at {api_url}")
    print(f"Using audio file: {audio_file_path}")
    
    # Check if the audio file exists
    if not os.path.exists(audio_file_path):
        print(f"Error: Audio file not found at {audio_file_path}")
        return False
    
    # Prepare the request
    headers = {
        "x-api-key": api_key
    }
    
    files = {
        "file": ("audio.mp3", open(audio_file_path, "rb"), "audio/mpeg")
    }
    
    try:
        # Send the request
        response = requests.post(api_url, headers=headers, files=files)
        
        # Check the response
        if response.status_code == 200:
            result = response.json()
            print("Transcription successful!")
            print(f"Transcribed text: {result['transcript']}")
            return True
        else:
            print(f"Error: API returned status code {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        # Close the file
        files["file"][1].close()

if __name__ == "__main__":
    # Default values
    api_url = "http://localhost:8000/transcribe"
    api_key = "MY_SUPER_SECRET"
    audio_file = "convo.mp3"
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        api_url = sys.argv[1]
    if len(sys.argv) > 2:
        api_key = sys.argv[2]
    if len(sys.argv) > 3:
        audio_file = sys.argv[3]
    
    # Run the test
    test_transcription_api(api_url, api_key, audio_file) 