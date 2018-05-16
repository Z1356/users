from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
