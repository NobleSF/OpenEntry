from django.db import models
from apps.common.abstract_models.base_category import BaseCategory


class StoreCategory(BaseCategory):
  """
  A seller's category set

  """
  store           = models.ForeignKey('store.Store', related_name='categories')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    verbose_name_plural = 'store categories'
    unique_together = ['store', 'name']
