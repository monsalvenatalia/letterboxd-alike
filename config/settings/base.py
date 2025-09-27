import os
import environ
env= environ.Env()
environ.Env.read_env()

DATABASES= {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'), 
        'HOST': env.str('POSTGRES_HOST'), 
        'PORT': env.int('POSTGRES_PORT'),
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
    'corsheaders'
]

LOCAL_APPS= [
    'configuration'
    'users', 
    'movies', 
]

INSTALLED_APPS= DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", 
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware", 
    "django.middleware.csrf.CsrfViewMiddleware", 
    "django.contrib.auth.middleware.AuthenticationMiddleware", 
    "django.contrib.messages.middleware.MessageMiddleware", 
    "django.middleware.clickjacking.XFrameOptionsMiddleware", 
    "whitenoise.middleware.WhiteNoiseMiddleware"
]

#CorsMiddleware should be placed as high as possible, especially before any middleware that can generate
#responses such as Django's CommonMiddleware or Whitenoise's WhiteNoiseMiddleware. If it is not before, it will not 
#be able to add the CORS headers to these responses

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

#here we will specify which servers will be able to connect to the backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]

MEDIA_ROOT= "/var/lib/django/data"
MEDIA_URL= "/media/"
STATICFILES_STORAGE= "whitenoise.storage.CompressedManifestStaticFilesStorage"
