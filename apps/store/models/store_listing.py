from django.db import models

from apps.common.abstract_models.base_listing import BaseListing


class StoreListing(BaseListing):
  """
  A unique listing belonging to a store.

  Inherites base model fields: product, currency, retail_price, sale_price, wholesale_price
  Inherits mixin fields: created_at, modified_at, published_at, unpublished_at, valid_at, expired_at, slug
  """
  store     = models.ForeignKey('store.Store', related_name='listings')


  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  class Meta:
    verbose_name_plural = 'store listings'
    ordering = ['-created_at',]
