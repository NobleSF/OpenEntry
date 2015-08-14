import os
from settings import LOCAL, STAGE, DEMO, PRODUCTION, INSTALLED_APPS

#Stormpath managed service for storing and accessing user data
INSTALLED_APPS += ('django_stormpath',)
AUTHENTICATION_BACKENDS = ('django_stormpath.backends.StormpathBackend',)
AUTH_USER_MODEL = 'django_stormpath.StormpathUser'
USE_ID_SITE = True # enables Stormpath Login pages


if not LOCAL:
  AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
  MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
  AWS_STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
  STATIC_ROOT = STATIC_URL = AWS_STATIC_URL
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

  # STORMPATH
  STORMPATH_ID = os.environ.get('STORMPATH_API_KEY_ID')
  STORMPATH_SECRET = os.environ.get('STORMPATH_API_KEY_SECRET')
  STORMPATH_APPLICATION = os.environ.get('STORMPATH_URL')
  from stormpath.cache.redis_store import RedisStore
  STORMPATH_CACHE_OPTIONS = {
    'store': RedisStore,
    'store_opts': {
      'host': os.environ.get('REDIS_URL').split(":")[2],
      'port': os.environ.get('REDIS_URL').split(":")[3]
    }
  }

  # #TRANSLOADIT
  # TRANSLOADIT_AUTH_KEY = os.environ.get('TRANSLOADIT_AUTH_KEY')
  # TRANSLOADIT_SECRET_KEY = os.environ.get('TRANSLOADIT_SECRET_KEY')
  # TRANSLOADIT_URL = os.environ.get('TRANSLOADIT_URL')
  # TRANSLOADIT_TEMPLATE_ID = os.environ.get('TRANSLOADIT_TEMPLATE_ID')
  #
  #
  # #SENDGRID EMAIL BACKEND
  # EMAIL_HOST          = 'smtp.sendgrid.net'
  # EMAIL_PORT          = 587
  # EMAIL_USE_TLS       = True
  # EMAIL_HOST_USER     = os.environ.get('SENDGRID_USERNAME')
  # EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')


else: #local dev, use local file: settings/local_environment_settings.py
  try:
    from local_environment_settings import *
  except:
    print """----------------------------------
          No local environment settings found!
          Create file settings/local_environment_settings.py
          See Tom for more information
          ----------------------------------"""
