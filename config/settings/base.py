import os

MEDIA_ROOT= "/var/lib/django/data"
MEDIA_URL= "/media/"

DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'), 
        'HOST': os.environ.get('POSTGRES_HOST'), 
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

DJANGO_APPS= [
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS= [
    'crispy_forms', 
    'django_countries', 
    'ckeditor', 
    'django_filters', 
    'rest_framework', 
    'rosetta', 
    'health_check'
]

LOCAL_APPS= [
    'configuration'
    'users', 
    'movies', 
]
