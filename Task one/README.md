# Speech-to-Text API

A FastAPI-based service that transcribes audio files using Groq's Whisper model.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Groq API key as an environment variable:
```bash
# Windows
set GROQ_API_KEY=your_groq_api_key_here

# Linux/Mac
export GROQ_API_KEY=your_groq_api_key_here
```

3. (Optional) Set a custom API key for authentication:
```bash
# Windows
set API_KEY=your_custom_api_key_here

# Linux/Mac
export API_KEY=your_custom_api_key_here
```

## Running the Server Locally

Start the server with:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at http://localhost:8000

## API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## Usage

Send a POST request to `/transcribe` with an audio file (WAV or MP3) in the request body and include the API key in the `x-api-key` header. The API will return the transcribed text in JSON format:

```json
{
    "transcript": "Your transcribed text here"
}
```

## Making the API Reachable by GHL

### Option A: Quick Tunnel (for testing)

#### Using ngrok:
```bash
ngrok http 8000
```

#### Using LocalTunnel:
```bash
lt --port 8000
```

### Option B: Deploy to Cloud (stable production URL)

#### Using Docker:
```bash
# Build the Docker image
docker build -t stt-api .

# Run the container
docker run -p 8080:8080 -e GROQ_API_KEY=your_groq_api_key -e API_KEY=your_custom_api_key stt-api
```

#### Deploy to Railway:
```bash
railway init && railway up
```

#### Deploy to Render:
1. Create a new "Web service"
2. Connect to your Git repository
3. Set the Start Command to: `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Add environment variables for `GROQ_API_KEY` and `API_KEY`

## Security

The API is secured with API key authentication. Include the API key in the `x-api-key` header with every request. The default key is "MY_SUPER_SECRET" but can be changed by setting the `API_KEY` environment variable.