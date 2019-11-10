import uuid
from django.db import models

from countries.models import Country


# Create your models here.
class Region(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=12, null=True, blank=True)
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.country.alpha_3_code, self.name)
