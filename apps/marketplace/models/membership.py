import uuid
from django.db import models
from django_extensions.db.fields.json import JSONField
from apps.common.behaviors import Timestampable, Permalinkable, Publishable, Expirable, Annotatable


class Membership(Timestampable, Expirable, Annotatable, models.Model):
  """
  A store's marketplace membership.

  Inherites mixin fields: created_at, modified_at, valid_at, expired_at, notes
  """
  id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  marketplace       = models.ForeignKey('marketplace.Marketplace')
  store             = models.ForeignKey('store.Store')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS


  class Meta:
    verbose_name_plural = 'memberships'
    ordering = ['created_at',]
