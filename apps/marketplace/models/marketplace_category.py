from django.db import models
from apps.common.abstract_models.base_category import BaseCategory


class MarketplaceCategory(BaseCategory):
  """
  A marketplace's category set

  """
  marketplace     = models.ForeignKey('marketplace.Marketplace', related_name='categories')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'marketplace categories'
    unique_together = ['marketplace', 'name']
