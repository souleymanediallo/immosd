from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos")
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Immo(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to="photos")
    photo_1 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_2 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_3 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_4 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_5 = models.ImageField(upload_to="photos", blank=True, null=True)
    photo_6 = models.ImageField(upload_to="photos", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


