from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=100)
    wine_type = models.CharField(max_length=50)
    year = models.IntegerField()
    region = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.year})"
