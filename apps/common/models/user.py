from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_stormpath.models import StormpathUser

class User(StormpathUser):
  REQUIRED_FIELDS = StormpathUser.REQUIRED_FIELDS
  REQUIRED_FIELDS = ['username']
  USERNAME_FIELD  = 'username'

  phone = models.CharField(max_length=16, blank=True, null=True)
