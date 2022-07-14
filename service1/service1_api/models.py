from django.db import models
from django.utils import timezone

class Basic_metals(models.Model):

    category = models.CharField(max_length=100)
    price = models.IntegerField()
    parity = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now,blank=False)
