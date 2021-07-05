from django.db import models

# Create your models here.
class Sales(models.Model):
    name = models.CharField(max_length=100)
    ogprice = models.FloatField(max_length=100)
    percentage = models.CharField(max_length=100)
    afprice = models.FloatField()
    def __str__(self):
        return self.name