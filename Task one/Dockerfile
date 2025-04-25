FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Set environment variables
ENV GROQ_API_KEY=""
ENV API_KEY="MY_SUPER_SECRET"

# Expose the port
EXPOSE 8080

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"] 