# devtool/models.py
from django.db import models

class DevTool(models.Model):
    name = models.CharField('이름',max_length=100)
    type = models.CharField('종류',max_length=100)
    description = models.TextField('설명')

    def __str__(self):
        return self.name
