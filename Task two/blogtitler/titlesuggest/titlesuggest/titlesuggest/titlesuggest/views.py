from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Initialize Django
if not settings.configured:
    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'rest_framework',
            'titlesuggest',
        ],
        REST_FRAMEWORK={
            'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.AllowAny',
            ]
        }
    )

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .model_handler import TitleGenerator

title_generator = TitleGenerator()

@api_view(['POST'])
def suggest_titles(request):
    content = request.data.get('content', '')
    if not content.strip():
        return Response({'error': 'Content cannot be empty'}, status=400)
    
    try:
        titles = title_generator.generate_titles(content)
        return Response({'titles': titles})
    except Exception as e:
        return Response({'error': str(e)}, status=500)