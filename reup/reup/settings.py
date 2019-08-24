import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('SECRET_KEY')

_hostname = os.environ.get('REUP_HOSTNAME')
if _hostname:
    REUP_BASE_URL = 'https://' + _hostname
    ALLOWED_HOSTS = ['localhost', _hostname]


def bool_env(value):
    return (value or '').lower() in ['on', 'true']


DEBUG = bool_env(os.environ.get('DEBUG'))

REUP_DOCUMENT_URL_PREFIX = os.environ.get('REUP_DOCUMENT_URL_PREFIX')

INSTALLED_APPS = [
    'revive.apps.ReviveConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'reup.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database/reup.sqlite',
    },
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'

if bool_env(os.environ.get('USE_X_FORWARDED_HOST')):
    USE_X_FORWARDED_HOST = True

_secure_header = os.environ.get('SECURE_PROXY_SSL_HEADER')
if _secure_header:
    SECURE_PROXY_SSL_HEADER = (_secure_header, 'https')
