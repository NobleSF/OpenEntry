import uuid
from django.db import models
from apps.common.behaviors import Timestampable


class Variant(models.Model):
  """
  A product's variations and related details

  """
  id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  product           = models.ForeignKey('store.Product')


  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'variants'
