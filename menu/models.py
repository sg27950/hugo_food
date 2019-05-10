from django.db import models
from datetime import datetime

class Menu(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    featured_listing = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    menu = models.ManyToManyField(Menu, related_name='categoryMenu')
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
