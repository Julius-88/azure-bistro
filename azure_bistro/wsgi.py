import os
from django.core.wsgi import get_wsgi_application

# This module is used by WSGI servers to serve the Django application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azure_bistro.settings')

application = get_wsgi_application()
