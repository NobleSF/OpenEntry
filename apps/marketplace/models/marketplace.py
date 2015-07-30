from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable, Permalinkable, Publishable


class Marketplace(Timestampable, Publishable, Permalinkable, models.Model):
  """
  A unique marketplace managed by one or more users and encompassing many stores.
  Able to edit which products from included stores are available, but not able to edit products directly.

  Inherites mixin fields: created_at, modified_at, published_at, unpublished_at, slug
  """

  name              = models.CharField(max_length=50)
  subdomain         = models.CharField(max_length=50)
  domain            = models.CharField(max_length=100)


  default_currency  = models.ForeignKey('common.Currency', null=True)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  def __unicode__(self):
    return unicode(self.title or self.id)

  class Meta:
    verbose_name_plural = 'marketplaces'
    ordering = ['created_at',]
