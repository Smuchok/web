from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    have_limit = models.BooleanField(default=False)

    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_all_cats', kwargs={'cat_id':self.pk})


class Goods(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=None)
    weight = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
