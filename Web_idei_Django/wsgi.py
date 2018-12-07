import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web_idei_Django.settings')

application = get_wsgi_application()
