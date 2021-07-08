from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Genres(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('genres_detail', kwargs={'pk': self.id})




class Sales(models.Model):
    name = models.CharField(max_length=100)
    ogprice = models.FloatField(max_length=100)
    percentage = models.CharField(max_length=100)
    afprice = models.FloatField()
    genres = models.ManyToManyField(Genres)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    class Meta:
        ordering = ['-date']
    