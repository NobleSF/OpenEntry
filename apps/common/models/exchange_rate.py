from django.db import models
from apps.common.behaviors import Timestampable


class ExchangeRate(Timestampable, models.Model):
  from_currency     = models.ForeignKey('common.Currency')
  to_currency       = models.ForeignKey('common.Currency')
  rate              = models.IntegerField()

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
  def __unicode__(self):
    return self.code
