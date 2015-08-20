from django.db import models
from apps.common.behaviors import Timestampable, Publishable, Permalinkable, Expirable, SEOable
from apps.common.utils import DollarField


class BaseListing(Timestampable, Publishable, Expirable, Permalinkable, SEOable, models.Model):
  product           = models.OneToOneField('store.Product')

  currency          = models.ForeignKey('common.Currency', null=True)
  retail_price      = DollarField(null=True, blank=True)
  sale_price        = DollarField(null=True, blank=True)
  wholesale_price   = DollarField(null=True, blank=True)


  title             = models.CharField(max_length=100, null=True, blank=True)
  description       = models.CharField(max_length=100, null=True, blank=True)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  def __unicode__(self):
    return unicode(self.title or self.pk)


  class Meta:
    abstract = True
