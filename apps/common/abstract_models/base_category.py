from django.db import models
from apps.common.behaviors import Timestampable, Permalinkable


class BaseCategory(Timestampable, Permalinkable, models.Model):
  """
  A category set. Can be used for stores or marketplaces.

  """
  name            = models.CharField(max_length=50)
  plural_name     = models.CharField(max_length=50)
  keywords        = models.CharField(max_length=50, null=True, blank=True)
  parent_category = models.ForeignKey('self', related_name='sub_categories', null=True)


  # MODEL PROPERTIES

  # MODEL FUNCTIONS

  class Meta:
    abstract = True
