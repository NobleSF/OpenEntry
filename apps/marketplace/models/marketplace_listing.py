from django.db import models

from apps.common.abstract_models.base_listing import BaseListing


class MarketplaceListing(BaseListing):
  """
  A unique listing belonging to a marketplace.

  Inherites base model fields: product, currency, retail_price, sale_price, wholesale_price
  Inherits mixin fields: created_at, modified_at, published_at, unpublished_at, valid_at, expired_at, slug
  """
  marketplace   = models.ForeignKey('marketplace.Marketplace', related_name='listings')


  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  class Meta:
    verbose_name_plural = 'marketplace listings'
    ordering = ['-created_at',]
