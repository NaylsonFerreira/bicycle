from pathlib import Path

from corsheaders.defaults import default_headers
from decouple import config as get_env
# from draft_project.logging import log_config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = get_env('DRAFT_SECRET_KEY', 'lc$a@$cy*xoabni2r=$28=3s-59@$')

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'djmoney',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'api_app.apps.ApiAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'draft_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'draft_project.wsgi.application'

ENGINE_DB = get_env('DRAFT_DB_ENGINE', 'mysql')

DATABASES = {
    'default': {
        'ENGINE': f"django.db.backends.{ENGINE_DB}",
        'NAME': get_env('DRAFT_DB_NAME', 'draft'),
        'USER': get_env('DRAFT_DB_USER', 'postgres'),
        'PASSWORD': get_env('DRAFT_DB_PASSWORD', ''),
        'HOST': get_env('DRAFT_DB_HOST', 'localhost'),
        'PORT': get_env('DRAFT_DB_PORT', '3306'),
    }
}

if ENGINE_DB == 'mysql':
    DATABASES['default']['OPTIONS'] = {'autocommit': True}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

ADMINS = [(
    'Administrative Team',
    get_env('DRAFT_SMTP_USER', 'admin@localhost.com')
)]

DEFAULT_FROM_EMAIL = get_env('DRAFT_SMTP_USER', 'admin@localhost.com')

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = get_env('DRAFT_SMTP_USER', 'admin@localhost.com')
    EMAIL_HOST_PASSWORD = get_env('DRAFT_SMTP_PASSWORD', 'password')

USE_I18N = True

USE_L10N = False
DATETIME_FORMAT = 'd/m/Y - G:i:s'
DATE_FORMAT = 'd/m/Y'
USE_TZ = False

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    'access-control-allow-origin',
    'access-control-allow-headers',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

if DEBUG:
    STATIC_FILES_DIRS = [
        str(BASE_DIR.joinpath('static')),
    ]
    STATIC_URL = '/static/'
else:
    STATIC_ROOT = get_env('DRAFT_STATIC_ROOT', 'static')
    STATIC_URL = get_env('DRAFT_STATIC_URL', '/static/')

MEDIA_URL = get_env('DRAFT_MEDIA_URL', '/media/')
MEDIA_ROOT = get_env('DRAFT_MEDIA_ROOT', 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FIXTURE_DIRS = ('fixtures', '')

# LOGGING = log_config()
