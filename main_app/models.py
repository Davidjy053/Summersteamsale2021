from django.db import models
from django.urls import reverse
# Create your models here.
class Sales(models.Model):
    name = models.CharField(max_length=100)
    ogprice = models.FloatField(max_length=100)
    percentage = models.CharField(max_length=100)
    afprice = models.FloatField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sales_id': self.id})

MODS = (
    ('U', 'Unofficial_patch'),
    ('G', 'Graphical_art'),
    ('A', 'Add_on')
)
class Mod(models.Model):
  date = models.DateField('Adding date')
  mods = models.CharField(max_length=1,  choices=MODS)
  sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_mods_display()} on {self.date}"
    