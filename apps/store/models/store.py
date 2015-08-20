from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable, Permalinkable, Publishable


class Store(Timestampable, Publishable, Permalinkable, models.Model):
  """
  A unique store managed by one or more users and owning several products.
  May not be publicly accessible or open for sales, but manages products nonetheless.

  Inherits mixin fields: created_at, modified_at, published_at, unpublished_at, slug
  """

  name              = models.CharField(max_length=50)
  subdomain         = models.CharField(max_length=50, null=True, blank=True)
  domain            = models.CharField(max_length=100, null=True, blank=True)

  default_currency  = models.ForeignKey('common.Currency', null=True)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  def __unicode__(self):
    return unicode(self.name or self.id)

  class Meta:
    verbose_name_plural = 'stores'
    ordering = ['created_at',]
