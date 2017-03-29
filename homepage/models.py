from django.db import models
from django.forms import ModelForm

# Create your models here.


# class Country(models.Model):
#     name = models.CharField(max_length=30)
#     capital = models.CharField(max_length=30)

class cover_image(models.Model):
    name = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)


class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to='', default='media/no-img.jpg')
    name = models.CharField(max_length=100, default='default', primary_key=True)
    # model_pic = models.ImageField(default = 'media/no-img.jpg')