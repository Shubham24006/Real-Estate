from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.utils.text import slugify
# from django.db.models.signals import post_delete
# from .utils import file_cleanup
# Create your models here.


class Property(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='properties')
    slug = models.SlugField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=1)
    photo_main = models.ImageField(upload_to='properties')
    photo_1 = models.ImageField(upload_to='properties', blank=True)
    photo_2 = models.ImageField(upload_to='properties', blank=True)
    photo_3 = models.ImageField(upload_to='properties', blank=True)
    photo_4 = models.ImageField(upload_to='properties', blank=True)
    photo_5 = models.ImageField(upload_to='properties', blank=True)
    photo_6 = models.ImageField(upload_to='properties', blank=True)
    is_rent = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.photo_main.delete()
        self.photo_1.delete()
        self.photo_2.delete()
        self.photo_3.delete()
        self.photo_4.delete()
        self.photo_5.delete()
        self.photo_6.delete()
        super().delete(*args, **kwargs)

# post_delete.connect(file_cleanup, sender=Property, dispatch_uid="property.photo_main.file_cleanup")
