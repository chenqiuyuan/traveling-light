from django.db import models

# Create your models here.
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)

