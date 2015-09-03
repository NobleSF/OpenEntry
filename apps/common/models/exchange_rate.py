import uuid
from django.db import models
from apps.common.behaviors import Timestampable


class ExchangeRate(Timestampable, models.Model):
  id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  from_currency     = models.ForeignKey('common.Currency', related_name='exchange_rates')
  to_currency       = models.ForeignKey('common.Currency')
  rate              = models.FloatField()

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
  def __unicode__(self):
    return self.code
