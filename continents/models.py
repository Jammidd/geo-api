from django.db import models


# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=2)

    def __str__(self):
        return '%s' % self.name