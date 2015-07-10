from django.db import models
from apps.common.behaviors.timestampable import Timestampable


class Address(Timestampable, models.Model):
  address       = models.CharField(max_length=100, blank=True, null=True)
  city          = models.CharField(max_length=35, blank=True, null=True)
  region        = models.CharField(max_length=35, blank=True, null=True)
  postal_code   = models.CharField(max_length=10, null=True, blank=True)

  # MODEL PROPERTIES
  @property
  def inline_string(self):
    string = "%s " % self.address
    string += "%s" % self.city or ""
    string += ", %s " % self.region or ""
    return string
    # return "%s %s, %s" % (self.address, self.city, self.state.abbreviation)

  @property
  def google_map_url(self):
    return "http://maps.google.com/?q=%s" % self.inline_string

  # MODEL FUNCTIONS
  def __unicode__(self):
    return unicode(self.inline_string)

  class Meta:
    verbose_name_plural = 'addresses'
