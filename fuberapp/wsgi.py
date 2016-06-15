import os
from django.core.wsgi import get_wsgi_application
default_django_settings_module = "fuberapp.settings.dev"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_django_settings_module)
application = get_wsgi_application()
