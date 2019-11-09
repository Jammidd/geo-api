import uuid
from django.db import models

from continents.models import Continent


class Country(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    continent = models.ForeignKey(Continent, related_name='countries', on_delete=models.CASCADE, null=True, blank=True)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    calling_code = models.CharField(max_length=4, null=True, blank=True)
    capital_city = models.CharField(max_length=100, null=True, blank=True)
    native_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name