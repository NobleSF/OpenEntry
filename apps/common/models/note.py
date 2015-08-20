from django.db import models
from apps.common.behaviors import Timestampable, Authorable


class Note(Timestampable, Authorable, models.Model):
  text = models.TextField(default="", blank=True)

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
