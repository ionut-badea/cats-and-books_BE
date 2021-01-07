import os
from pathlib import Path
import logging.config
from dotenv import load_dotenv
from envtypes import EnvTypes
from corsheaders.defaults import default_headers, default_methods

load_dotenv()
et = EnvTypes(use_prefix=False)

# General settings
BASE_DIR = Path(__file__).resolve().parent.parent


# CORS
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CORS_ALLOWED_ORIGINS = ['http://127.0.0.2:3000',
                        'https://cats-and-books.netlify.app']


# DataBase
DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{et.set_env("DB_ENGINE")}',
        'NAME': et.set_env("DB_NAME"),
        'USER': et.set_env("DB_USER"),
        'PASSWORD': et.set_env("DB_PASSWORD"),
        'HOST': et.set_env("DB_HOST"),
        'PORT': et.set_env("DB_PORT"),
    }
}


# Debugging
DEBUG = True if et.set_env('DEBUG') else False


# Email
ADMINS = [et.set_env('ADMINS')]
MANAGERS = ADMINS


# Files
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Globalization
FIRST_DAY_OF_WEEK = 1
LANGUAGE_CODE = 'en-us'


# GraphQL
GRAPHENE = {
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_ALGORITHM': 'HS512',
    'JWT_SECRET_KEY': et.set_env('JWT_SECRET_KEY'),
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_REFRESH_EXPIRED_HANDLER': lambda orig_iat, context: False,
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
LOGLEVEL = 'ERROR' if not DEBUG else 'INFO'
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
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'cats-and-books.herokuapp.com']
AUTH_USER_MODEL = 'accounts.User'
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
        'OPTIONS': {
            'min_length': 12
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
CSRF_COOKIE_AGE = 31449600
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True if not DEBUG else False
CSRF_USE_SESSIONS = False
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher'
]
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_HTTPONLY = True if not DEBUG else False
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True if not DEBUG else False
SECRET_KEY = et.set_env('SECRET_KEY')
SECURE_HSTS_SECONDS = 3600 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True if not DEBUG else False
SECURE_SSL_REDIRECT = True if not DEBUG else False
SECURE_REFERRER_POLICY = 'origin-when-cross-origin'


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
ROOT_URLCONF = 'blog.urls'
