from django.db import models


class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.TextField(null=True)

    def __str__(self):
        return self.name
