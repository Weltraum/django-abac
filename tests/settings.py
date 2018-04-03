import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

DEBUG_PROPAGATE_EXCEPTIONS = True

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'abac',
    'tests',
]

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'abac.middleware.ABACMiddleware',
)


ABAC_SETTINGS = {
    'DEFAULT_AUTHENTICATION': True,
    'ADDITIONAL_AUTHENTICATION_CLASS': (
        'abac.authentication.RestFrameworkBasicAuthentication',
        'abac.authentication.RestFrameworkSessionAuthentication',
        'abac.authentication.RestFrameworkTokenAuthentication',
        'abac.authentication.RestFrameworkRemoteUserAuthentication',
        'abac.authentication.RestFrameworkJSONWebTokenAuthentication',
    ),
}


MIDDLEWARE_CLASSES = MIDDLEWARE,

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            "debug": True,  # We want template errors to raise
        }
    },
]

PASSWORD_HASHERS=(
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

ROOT_URLCONF = 'tests.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_URL

USE_I18N = True

USE_L10N = True