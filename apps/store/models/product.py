import uuid
from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable


class Product(Timestampable, models.Model):
  """
  A unique product belonging to a store. Has limited quantity with shared mutability by many possible points of sale

  Inherits mixin fields: created_at, modified_at

  some categories may auto-assign specific option_sets
  """
  id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  store             = models.ForeignKey('store.Store', related_name='products')
  quantity          = models.IntegerField(default=0)

  #product description elements
  name              = models.CharField(max_length=50, null=True, blank=True)
  description       = models.CharField(max_length=50, null=True, blank=True)
  categories        = models.ManyToManyField('store.StoreCategory', related_name='products')
  colors            = JSONField(default="", blank=True)

  width             = models.FloatField(null=True) #in meters
  height            = models.FloatField(null=True) #in meters
  length            = models.FloatField(null=True) #in meters
  weight            = models.FloatField(null=True) #in grams

  price             = models.IntegerField(null=True) #in units of defined currency
  currency          = models.ForeignKey('common.Currency', null=True) #default to self.store.default_currency

  shipping_options  = models.ManyToManyField('store.ShippingOption')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  class Meta:
    verbose_name_plural = 'products'
    ordering = ['-created_at',]
