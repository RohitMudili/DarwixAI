# DarwixAI
## Task 1: Overview

Task 1 focuses on establishing the foundational components of the DarwixAI project. This task is critical for setting the stage for future development and ensuring a robust and scalable architecture.

### Objectives
- **Define the Core Architecture**: Establish a modular and scalable architecture that supports future enhancements.
- **Implement Initial Features**: Develop the essential features required for the project's foundation.
- **Ensure Scalability**: Design the system to accommodate future tasks and integrations seamlessly.

### Steps
1. **Set Up the Development Environment**:
    - Install necessary tools and dependencies.
    - Configure version control and CI/CD pipelines.
2. **Create the Base Project Structure**:
    - Define folder structures and naming conventions.
    - Set up configuration files and initial boilerplate code.
3. **Implement and Test Core Functionalities**:
    - Develop the primary modules and components.
    - Write unit tests and perform integration testing.

### Deliverables
- A functional prototype of the foundational components.
- Comprehensive documentation covering:
  - Setup instructions.
  - Usage guidelines.
  - Architectural decisions.

### Timeline
- **Estimated Completion**: 1 Hour.
- **Milestones**:
  - Week 1: Environment setup and project structure creation.
  - Week 2: Core functionalities implementation and testing.

### Notes
- Adhere to the project's coding standards and best practices.
- Ensure all code is thoroughly tested and reviewed before submission.
- Document any challenges or deviations from the initial plan for future reference.
- Use version control effectively to track progress and collaborate efficiently.
- Regularly update the team on progress during stand-up meetings or via the project management tool.
- Seek feedback on the prototype to refine and improve the implementation.

Task 2

🧠 Blog Title Suggestion API with Django & Hugging Face Transformers

This project is a RESTful API built with Django and Django REST Framework that suggests catchy blog titles using a Hugging Face transformer model (GPT-2 by default).

---

## 🚀 Features

- Accepts blog content via a POST request
- Generates 3 relevant title suggestions using NLP
- Runs locally using Django development server
- Easily extendable to other text generation models

---

## 🏗️ Project Structure

blogtitler/ ├── blogtitler/ │ ├── init.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── titlesuggest/ │ ├── init.py │ ├── views.py │ ├── model_handler.py │ ├── urls.py │ └── apps.py ├── manage.py ├── run.py ├── requirements.txt └── README.md

yaml
Copy
Edit

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/blogtitler.git
cd blogtitler
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚙️ Setup
1. Apply migrations
bash
Copy
Edit
python manage.py migrate
2. Run the development server
bash
Copy
Edit
python manage.py runserver
Server will be live at: http://127.0.0.1:8000/

🔁 API Usage
Endpoint
bash
Copy
Edit
POST /api/suggest-titles/
Request Body
json
Copy
Edit
{
  "content": "Your blog post content goes here..."
}
Sample cURL
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/suggest-titles/ \
-H "Content-Type: application/json" \
-d '{"content":"A guide to deploying ML models in Django apps."}'
Response
json
Copy
Edit
{
  "titles": [
    "Deploying Machine Learning Models with Django",
    "How to Serve ML Models in Django Applications",
    "End-to-End ML Deployment with Django Framework"
  ]
}
🧪 Local Testing Without Server
You can also run a test script without starting the Django server:

bash
Copy
Edit
python run.py
This uses Django's test framework to send a simulated request and prints the output directly in the console.

🧠 Model Details
Uses Hugging Face transformers pipeline

Default model: gpt2

Easily replaceable with models like tiiuae/falcon, google/flan-t5-base, etc.

📌 Requirements
Python 3.8+

Django 4.x

Transformers

Torch

Django REST Framework

See requirements.txt for versions.

🧰 Extending the Project
Swap gpt2 with other Hugging Face models

Add authentication or rate limiting

Integrate a frontend (e.g., React or HTML)

Deploy using Docker, Gunicorn, or on cloud platforms

📄 License
This project is licensed under the MIT License.
