from django.db import models
from django_stormpath.models import StormpathUser

class Authorable(models.Model):

  author          = models.ForeignKey(StormpathUser)
  authored_at     = models.DateTimeField(null=True, blank=True)

  class Meta:
    abstract = True
