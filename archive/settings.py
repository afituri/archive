"""
Django settings for archive project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#importing json lib
import json
from pprint import pprint


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7j8s-y_j7&l0x5(bl5svb-!gs)9cn@!*vez$&h=(@i)yn9@4)v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hnec',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'archive.urls'

WSGI_APPLICATION = 'archive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

json_data=open('archive/config.json')
data = json.load(json_data)
json_data.close()
DATABASES = {
    'default': {
        'ENGINE': data["ENGINE"],
        'NAME': data["NAME"],                     
        'USER': data["USER"],
        'PASSWORD': data["PASSWORD"],
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db',                     
#         'USER': 'anas',
#         'PASSWORD': '123',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
TEMPLATE_DIRS=(
    os.path.join(os.path.dirname(BASE_DIR),"archive", "static","template"), # this is where we put all of our templates
    #'/home/anas/django/archive/static/Template'

    )
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"archive", "static","static-only")
FILES_ROOT = os.path.join(os.path.dirname(BASE_DIR),"archive", "static","Files") #where we collect static files such as (css,jquery)
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"archive", "static","media") #where we store the media uploaded by yser
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR),"archive", "static","static"),
    os.path.join(os.path.dirname(BASE_DIR),"archive", "static"),

    )
