from django.db import models


class Continent(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Country(models.Model):
    common_name = models.CharField(max_length=159, blank=True)
    formal_name = models.CharField(max_length=159, blank=True)
    common_name_fr = models.CharField(max_length=159, blank=True)
    formal_name_fr = models.CharField(max_length=159, blank=True)
    iso3166a2 = models.CharField(max_length=6, blank=True)
    iso3166a3 = models.CharField(max_length=9,blank=True)
    iso3166n3 = models.IntegerField(null=True, blank=True)
    continent = models.ForeignKey(Continent, blank=True, null=True)
    centroid_latitude = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    centroid_longitude = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)

    def __unicode__(self):
        return u'%s (%s)' % (self.common_name, self.iso3166a2)

    class Meta:
        verbose_name ='Country'
        verbose_name_plural = 'Countries'
        ordering = ('common_name',)

