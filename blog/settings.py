import os
import logging.config
from dotenv import load_dotenv
from datetime import timedelta
from distutils.util import strtobool
from corsheaders.defaults import default_headers, default_methods

load_dotenv()

# General settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# CORS
CORS_ALLOW_CREDENTIALS = bool(
    strtobool(os.getenv('DJANGO_CORS_ALLOW_CREDENTIALS')))

CORS_ALLOW_HEADERS = list(default_headers)

CORS_ALLOW_METHODS = list(default_methods)

CORS_ORIGIN_ALLOW_ALL = bool(
    strtobool(os.getenv('DJANGO_CORS_ORIGIN_ALLOW_ALL')))

CORS_ORIGIN_WHITELIST = os.getenv('DJANGO_CORS_ORIGIN_WHITELIST').split(',')

# DataBase
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(
            os.getenv('DJANGO_DEFAULT_DATABASE_ENGINE')
        ),
        'NAME': os.getenv('DJANGO_DEFAULT_DATABASE_NAME'),
        'USER': os.getenv('DJANGO_DEFAULT_DATABASE_USER'),
        'PASSWORD': os.getenv('DJANGO_DEFAULT_DATABASE_PASSWORD'),
        'HOST': os.getenv('DJANGO_DEFAULT_DATABASE_HOST'),
        'PORT': os.getenv('DJANGO_DEFAULT_DATABASE_PORT'),
    }
}


# Debugging
DEBUG = bool(strtobool(os.getenv('DJANGO_DEBUG')))

# Email
ADMINS = os.getenv('DJANGO_ADMINS')
MANAGERS = ADMINS


# Files
MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv('DJANGO_MEDIA_ROOT'))

MEDIA_URL = os.getenv('DJANGO_MEDIA_URL')

STATIC_ROOT = os.path.join(BASE_DIR, os.getenv('DJANGO_STATIC_ROOT'))

STATIC_URL = os.getenv('DJANGO_STATIC_URL')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Globalization
FIRST_DAY_OF_WEEK = int(os.getenv('DJANGO_FIRST_DAY_OF_WEEK'))

LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE')


# GraphQL
GRAPHENE = {
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_ALGORITHM': os.getenv('DJANGO_JWT_ALGORITHM'),
    'JWT_ALLOW_ARGUMENT':
        bool(strtobool(os.getenv('DJANGO_JWT_ALLOW_ARGUMENT'))),
    'JWT_EXPIRATION_DELTA':
        timedelta(minutes=int(os.getenv('DJANGO_JWT_EXPIRATION_DELTA'))),
    'JWT_LONG_RUNNING_REFRESH_TOKEN':
        bool(strtobool(os.getenv('DJANGO_JWT_LONG_RUNNING_REFRESH_TOKEN'))),
    'JWT_REFRESH_EXPIRED_HANDLER': lambda orig_iat, context: False,
    'JWT_REFRESH_EXPIRATION_DELTA':
        timedelta(days=int(os.getenv('DJANGO_JWT_REFRESH_EXPIRATION_DELTA'))),
    'JWT_SECRET_KEY': os.getenv('DJANGO_JWT_SECRET_KEY'),
    'JWT_VERIFY': bool(strtobool(os.getenv('DJANGO_JWT_VERIFY'))),
    'JWT_VERIFY_EXPIRATION':
        bool(strtobool(os.getenv('DJANGO_JWT_VERIFY_EXPIRATION'))),
}

# HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Logging
LOGGING_CONFIG = None

LOGLEVEL = os.getenv('DJANGO_LOGLEVEL').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(process)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console', ],
        },
    },
})


# Models
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'corsheaders',
    'storages',
    'accounts',
    'contacts',
    'posts',
    'subscription'
]


# Security
# ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')
ALLOWED_HOSTS = ['localhost', 'cats-and-books.herokuapp.com']
AUTH_USER_MODEL = os.getenv('DJANGO_AUTH_USER_MODEL')

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CSRF_COOKIE_AGE = int(os.getenv('DJANGO_CSRF_COOKIE_AGE'))
CSRF_COOKIE_HTTPONLY = bool(
    strtobool(os.getenv('DJANGO_CSRF_COOKIE_HTTPONLY')))
CSRF_COOKIE_SAMESITE = os.getenv('DJANGO_CSRF_COOKIE_SAMESITE')
CSRF_COOKIE_SECURE = bool(strtobool(os.getenv('DJANGO_CSRF_COOKIE_SECURE')))
CSRF_USE_SESSIONS = bool(strtobool(os.getenv('DJANGO_CSRF_USE_SESSIONS')))

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher'
]

SESSION_COOKIE_AGE = int(os.getenv('DJANGO_SESSION_COOKIE_AGE'))
SESSION_COOKIE_HTTPONLY = bool(
    strtobool(os.getenv('DJANGO_SESSION_COOKIE_HTTPONLY')))
SESSION_COOKIE_SAMESITE = os.getenv('DJANGO_SESSION_COOKIE_SAMESITE')
SESSION_COOKIE_SECURE = bool(
    strtobool(os.getenv('DJANGO_SESSION_COOKIE_SECURE')))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECURE_BROWSER_XSS_FILTER = os.getenv('DJANGO_SECURE_BROWSER_XSS_FILTER')
SECURE_HSTS_SECONDS = int(os.getenv('DJANGO_SECURE_HSTS_SECONDS'))
SECURE_SSL_REDIRECT = bool(strtobool(os.getenv('DJANGO_SECURE_SSL_REDIRECT')))
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(
    strtobool(os.getenv('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS')))
SECURE_REFERRER_POLICY = bool(strtobool(
    os.getenv('DJANGO_SECURE_REFERRER_POLICY')))
SECURE_HSTS_PRELOAD = bool(strtobool(os.getenv('DJANGO_SECURE_HSTS_PRELOAD')))

# Templates
TEMNPALTES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMNPALTES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# URLs
ROOT_URLCONF = os.getenv('DJANGO_ROOT_URLCONF')
