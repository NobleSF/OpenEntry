from django.db import models
from apps.common.behaviors import Timestampable


class ShippingOption(Timestampable, models.Model):
  """
  A products's available shipping options and costs


  to_country
  min_days
  max_days
  cost
  """

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'shipping options'
