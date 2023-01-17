from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=10)
    # Will be used to store a json representation of the times
    # [ {day: M, starttime: 900, endtime: 990} ]
    times = models.JSONField()

    def __str__(self):
        return f'{self.name} - {self.shortcode}'