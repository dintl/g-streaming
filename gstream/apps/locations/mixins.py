from django.db import models
from .models import Country

class LocationMixin(models.Model):
    latitude     = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=5
    )
    longitude     = models.DecimalField(
        null=True, blank=True, max_digits=8, decimal_places=5
    )
    show_precise = models.BooleanField(default=True)

    country = models.ForeignKey(Country, blank=True, null=True)

    class Meta:
    	abstract=True