from django.db import models

class CarStatus(models.Model):
    speed = models.IntegerField()
    fuel = models.IntegerField()
    temperature = models.IntegerField()
    range_km = models.IntegerField()
    gear = models.CharField(max_length=2)
    song = models.CharField(max_length=100)

    def __str__(self):
        return f"Car Status - Speed {self.speed}"
