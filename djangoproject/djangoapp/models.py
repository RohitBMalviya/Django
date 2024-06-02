from django.db import models
from django.utils import timezone

# Create your models here.

class ModelExample(models.Model):
    ENUMSEXAMPLE = [
        ('EM1','ENUM1'),
        ('EM2','ENUM2'),
        ('EM3','ENUM3'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='models/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4,choices=ENUMSEXAMPLE)
    description = models.TextField(default="")
    prices = models.IntegerField(default=0)

    def __str__(self):
        return self.name