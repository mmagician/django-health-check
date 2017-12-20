
import os.path
import uuid

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'health_check',
    'health_check.cache',
    'health_check.db',
    'health_check.storage',
    'health_check.contrib.celery',
    'health_check.contrib.s3boto_storage',
    'tests',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_ID = 1
ROOT_URLCONF = 'tests.testapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
        }
    },
]

SECRET_KEY = uuid.uuid4().hex

USE_L10N = True

CELERY_QUEUES = {
    'default': {
        'exchange': 'default',
        'binding_key': 'default',
        'display_name': 'Celery queue 1'
    },
    'queue2': {
        'exchange': 'queue2',
        'binding_key': 'queue2',
        'display_name': 'Celery queue 2'
    }
}
