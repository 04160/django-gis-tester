from django.db import models


class LocationModel(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'coordinates_location'
