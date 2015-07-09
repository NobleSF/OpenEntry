"""
Django settings for OpenEntry project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

#DEFINE THE ENVIRONMENT TYPE
PRODUCTION = STAGE = DEMO = LOCAL = False
if not os.environ.get('APP_NAME'):
  LOCAL = True
elif '-demo' == os.environ.get('APP_NAME')[-5:]:
  DEMO = True
elif '-stage' == os.environ.get('APP_NAME')[-6:]:
  STAGE = True
else:
  PRODUCTION = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL or STAGE
TEMPLATE_DEBUG = LOCAL

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'apps.common',
)
# 3rd Party Services
INSTALLED_APPS += (
    'django_stormpath',
)
#Django Services
INSTALLED_APPS += (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
)
# if LOCAL or STAGE:
#   INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Static files (CSS, JavaScript, Images) https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'


if LOCAL:
  MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)

#AUTOMATED AND UNIT TESTING
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

# DATABASE https://docs.djangoproject.com/en/1.7/ref/settings/#databases
import dj_database_url
if PRODUCTION or STAGE:
  DATABASES = {'default': dj_database_url.config()}
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
  from local_environment_settings import DATABASES

# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'UTC'
USE_TZ = True

#3RD PARTY SERVICES SETTINGS
from vendor_services_settings import *
