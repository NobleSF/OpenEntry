from django.db import models
from apps.common.behaviors import Timestampable, Publishable, Permalinkable, Expirable
from apps.common.utils import DollarField


class BaseListing(Permalinkable, Publishable, Timestampable, Expirable, models.Model):
  product           = models.OneToOneField('seller.Product')

  retail_price      = DollarField()
  wholesale_price   = DollarField()


  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  class Meta:
    abstract = True
