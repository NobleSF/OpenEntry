from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable


class Product(Timestampable, models.Model):
  """
  A unique product belonging to a store. Has limited quantity with shared mutability by many possible points of sale

  Inherits mixin fields: created_at, modified_at

  some categories may auto-assign specific option_sets
  """

  store         = models.ForeignKey('store.Store')
  quantity      = models.IntegerField(default=0)



  #product description elements
  categories    = models.ManyToManyField('store.Category', related_name='products')
  colors        = JSONField()

  width         = models.FloatField(null=True) #in meters
  height        = models.FloatField(null=True) #in meters
  length        = models.FloatField(null=True) #in meters
  weight        = models.FloatField(null=True) #in grams

  price         = models.IntegerField(null=True) #in units of defined currency
  currency      = models.ForeignKey('common.Currency', null=True) #default to self.store.default_currency

  option_sets   = models.ManyToManyField('store.OptionSet', related_name='products')

  shipping_options = models.ManyToManyField('store.ShippingOption')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  def __unicode__(self):
    return unicode(self.title or self.id)

  class Meta:
    verbose_name_plural = 'products'
    ordering = ['-created_at',]
