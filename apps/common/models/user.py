from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_stormpath.models import StormpathUser
from apps.common.behaviors.locatable import Locatable
from apps.common.behaviors.timestampable import Timestampable


# class User(Timestampable, Locatable, StormpathUser):
#   REQUIRED_FIELDS = StormpathUser.REQUIRED_FIELDS
#   REQUIRED_FIELDS = ['username']
#   USERNAME_FIELD  = 'username'
#
#   phone = models.CharField(max_length=16, null=True)




#
# STORMPATH NOTES
# ====================================================================
#
# Python Documentation: http://docs.stormpath.com/python/
#
# Python-specific Blog posts:
#
# -https://stormpath.com/blog/improving-our-python-support/
# -https://stormpath.com/blog/making-python-authentication-fast/
# -https://stormpath.com/blog/stormpath-and-django/
# -https://stormpath.com/blog/hosted-login-and-api-authentication-for-python/
# -https://stormpath.com/blog/flask-auth-in-one-loc/
#
