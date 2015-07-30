from django.db import models
from apps.common.behaviors import Timestampable


class Currency(Timestampable, models.Model):
  name                  = models.CharField(max_length=50)
  code                  = models.CharField(max_length=3)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
  def __unicode__(self):
    return self.code
