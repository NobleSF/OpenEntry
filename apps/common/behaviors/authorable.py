from django.db import models


class Authorable(models.Model):

  author          = models.ForeignKey('common.User')
  authored_at     = models.DateTimeField(null=True)

  class Meta:
    abstract = True
