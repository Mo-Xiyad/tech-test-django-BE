from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    # date_created = models.DateTimeField(default=datetime.now, blank=True)

class Categories(models.TextChoices):
    SPORTSWEAR = 'sportswear'
    OFFICEWEAR = 'officewear'
    CASUALWEAR = 'casualWear'
    SUMMERWEAR = 'summerwear'
    WINTERWEAR = 'winterwear'
    BEACHWEAR = 'beachwear'


class HotListModel(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=100, choices=Categories.choices, default=Categories.CASUALWEAR)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')#its going to be organised by Year Month Day
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if self.featured:
            try:
                temp = HotListModel.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except HotListModel.DoesNotExist:
                pass
        
        super(HotListModel, self).save(*args, **kwargs)

    def __str__(self): #string representation of the model by title
        return self.title