from django.db import models
from apps.common.behaviors import Timestampable, Authorable


class Note(Timestampable, Authorable, models.Model):
  text = models.TextField(default="")

  # MODEL PROPERTIES

  # MODEL FUNCTIONS
