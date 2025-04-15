import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogtitler.settings')
django.setup()

from titlesuggest.views import suggest_titles
from rest_framework.test import APIRequestFactory

# Test the view directly
if __name__ == '__main__':
    factory = APIRequestFactory()
    request = factory.post(
        '/api/suggest-titles/',
        {'content': 'How to integrate NLP with Django'},
        format='json'
    )
    response = suggest_titles(request)
    print(response.data)