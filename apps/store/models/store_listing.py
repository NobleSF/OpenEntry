from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable, Permalinkable, Publishable


class StoreListing(Timestampable, Publishable, Permalinkable, models.Model):
  """
  A unique product belonging to a store. Has limited quantity with shared mutability by many possible points of sale

  Inherites mixin fields: created_at, modified_at, published_at, unpublished_at, slug

  some categories may auto-assign specific option_sets
  """

  store         = models.ForeignKey('store.Store')
  quantity      = models.IntegerField(default=0)

  title         = models.CharField(max_length=100, blank=True, null=True)
  description   = models.CharField(max_length=100, blank=True, null=True)

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

  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  def __unicode__(self):
    return unicode(self.title or self.id)

  class Meta:
    verbose_name_plural = 'products'
    ordering = ['-created_at',]
