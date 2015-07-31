from django.db import models
from apps.common.abstract_models.base_category import BaseCategory


class CategoryEquivelence(models.Model):
  """
  A marketplace's category set

  """
  marketplace_category  = models.ForeignKey('marketplace.MarketplaceCategory')
  store_category        = models.ForeignKey('store.StoreCategory')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'category equivelencies'
    unique_together = ['marketplace_category', 'store_category']
