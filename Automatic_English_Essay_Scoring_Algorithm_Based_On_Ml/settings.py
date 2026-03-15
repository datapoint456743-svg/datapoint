import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECURITY ---------------- #

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key')  # Get from environment variable

DEBUG = False  # Set to False in production

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# ---------------- APPLICATIONS ---------------- #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise',  # Ensure whitenoise is included
    'admins',
    'users',
]

# ---------------- MIDDLEWARE ---------------- #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # To serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Automatic_English_Essay_Scoring_Algorithm_Based_On_Ml.urls'

# ---------------- TEMPLATES ---------------- #

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Automatic_English_Essay_Scoring_Algorithm_Based_On_Ml.wsgi.application'

# ---------------- DATABASE ---------------- #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change to PostgreSQL for production
        'NAME': os.environ.get('DB_NAME', 'default_db_name'),
        'USER': os.environ.get('DB_USER', 'default_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'default_password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# ---------------- PASSWORD VALIDATION ---------------- #

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

# ---------------- INTERNATIONALIZATION ---------------- #

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# ---------------- STATIC FILES ---------------- #

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------- MEDIA FILES ---------------- #

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# ---------------- RENDER SECURITY ---------------- #

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS

# ---------------- CSRF FIX FOR RENDER ---------------- #

CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']

# ---------------- DEFAULT PRIMARY KEY ---------------- #

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------- LOGGING ---------------- #

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
