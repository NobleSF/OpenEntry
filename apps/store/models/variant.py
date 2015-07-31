from django.db import models
from apps.common.behaviors import Timestampable


class Variant(models.Model):
  """
  A product's variations and related details

  """
  product   = models.ForeignKey('store.Product')


  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'variants'
