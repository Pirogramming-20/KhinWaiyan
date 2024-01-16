# models.py
from django.db import models

class LocalUser(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField(default=20)

    def __str__(self):
        return self.name