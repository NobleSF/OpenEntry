from django.db import models

class Country(models.Model): #could expand on pypi.python.org/pypi/django-countries
  name          = models.CharField(max_length=100)
  code          = models.CharField(max_length=3)
  calling_code  = models.CharField(max_length=3)
  # assuming countries stick to one currency nationwide

  # currency      = models.IntegerField()
  currency      = models.ForeignKey('common.Currency', related_name='countries')

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
  def __unicode__(self):
    return self.code

  class Meta:
    verbose_name_plural = 'countries'
