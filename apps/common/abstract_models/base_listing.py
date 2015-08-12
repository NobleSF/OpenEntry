from django.db import models
from apps.common.behaviors import Timestampable, Publishable, Permalinkable, Expirable, SEOable
from apps.common.utils import DollarField


class BaseListing(Timestampable, Publishable, Expirable, Permalinkable, SEOable, models.Model):
  product           = models.OneToOneField('store.Product')

  currency          = models.ForeignKey('common.Currency')
  retail_price      = DollarField()
  sale_price        = DollarField()
  wholesale_price   = DollarField()


  title             = models.CharField(max_length=100, null=True)
  description       = models.CharField(max_length=100, null=True)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  def __unicode__(self):
    return unicode(self.title or self.pk)


  class Meta:
    abstract = True
