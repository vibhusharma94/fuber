# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os.path import abspath, dirname, join, normpath
from sys import path

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(^%b-f1+dp-uu06qf9*^f+-#2dykcore7$e0_$(qqeoh79+(dz'

DEBUG = True

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    'apps.home',
    'apps.apis.fuber',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'fuberapp.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)

WSGI_APPLICATION = 'fuberapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fuberdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True


STATIC_ROOT_DIR = 'static'
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, STATIC_ROOT_DIR)),
)
STATIC_URL = '/static/'

MEDIA_ROOT_DIR = 'media'
MEDIA_ROOT = normpath(join(DJANGO_ROOT, MEDIA_ROOT_DIR))
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
