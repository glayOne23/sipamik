"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv # https://github.com/henriquebastos/python-decouple
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*9ha6lr!szcpsq6f!xdqw2c-x1@(ckd863a%69behmev5z)%2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django',
    # ======[External Apps]======
    'django_cas_ng',
    'hijack.contrib.admin',
    'hijack',    
    "crispy_forms",
    "crispy_bootstrap4",
    # =======[My Own Apps]=======
    "pendampingan"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_cas_ng.middleware.CASMiddleware',
    'hijack.middleware.HijackUserMiddleware',    
]

ROOT_URLCONF = 'project.urls'

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

                'services.context_processors.global_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE'     : config('DB_ENGINE',   default='django.db.backends.postgresql'),
       'NAME'       : config('DB_NAME',     default='YOUR_DB_NAME'),
       'USER'       : config('DB_USER',     default='YOUR_DB_USER'),
       'PASSWORD'   : config('DB_PASSWORD', default='YOUR_DB_PASSWORD'),
       'HOST'       : config('DB_HOST',     default='127.0.0.1'),
       'PORT'       : config('DB_PORT',     default='5432', cast=int),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

ON_PRODUCTION = config('ON_PRODUCTION',   default=False),


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

if ON_PRODUCTION:
    STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"


# =====[Media Files]=====
MEDIA_ROOT              = os.path.join(BASE_DIR,'media')
MEDIA_URL               = '/media/'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)


# ======[Login URL]======
LOGIN_URL               = '/signin'
LOGIN_REDIRECT_URL      = '/signin'


# ======[Django Cas]=====
CAS_SERVER_URL          = 'https://auth.ums.ac.id/cas/'
CAS_ADMIN_PREFIX        = 'admin' # Set to -> '/admin' if you want to login to the admin using cas
CAS_CREATE_USER         = True
CAS_LOGIN_MSG           = 'Login succeeded. Welcome, %s.'
CAS_LOGGED_MSG          = 'You are logged in as %s.'
CAS_LOGIN_URL_NAME      = 'cas_ng_login'
CAS_LOGOUT_URL_NAME     = 'cas_ng_logout'
CAS_LOGOUT_COMPLETELY   = True
CAS_IGNORE_REFERER      = True
CAS_REDIRECT_URL        = '/signin' # The default is '/'
CAS_VERSION             = '2'


# =======[App Info]======
APP_SIDEBAR_NAME          = 'CG'
APP_SHORT_NAME          = 'SIPAMIK'
APP_FULL_NAME           = 'SIPAMIK'
APP_VERSION             = 'v1.0'
APP_YEAR                = '2024'
APP_DEVELOPER           = 'BTI'
APP_COMPANY_SHORT_NAME  = 'UMS'
APP_COMPANY_FULL_NAME   = 'Universitas Muhammadiyah Surakarta'
# APP_LOGO                = os.path.join(STATIC_URL,'images/logo/ums_logo_color.svg')
# APP_FAVICON             = os.path.join(STATIC_URL,'images/logo/ums_logo_favicon.ico')
APP_LOGO                = os.path.join(STATIC_URL,'images/logo/logo2.png')
APP_FAVICON             = os.path.join(STATIC_URL,'images/logo/logo2.png')
APP_BASE_URL            = config('APP_BASE_URL', default='') # for email verify


# =====[API GATEWAY]=====
# It is used to sync cas login data with Sihrd API (apps.services.utils.profilesync)
# if you don't have an apigateway account, please create an account at https://api.ums.ac.id/admin/
API_GATEWAY_URL         = config('API_GATEWAY_URL',      default='https://api.ums.ac.id/') # or -> http://172.16.10.241:8008/
API_GATEWAY_USERNAME    = config('API_GATEWAY_USERNAME', default='YOUR_APIGATEWAY_USERNAME')
API_GATEWAY_PASSWORD    = config('API_GATEWAY_PASSWORD', default='YOUR_APIGATEWAY_PASSWORD')