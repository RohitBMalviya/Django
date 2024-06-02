from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# One to Many

class ExampleReview(models.Model):
    exampleForeignKey = models.ForeignKey(ModelExample,on_delete=models.CASCADE,related_name="exampleReviews")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    commet = models.TextField()
    data_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.exampleForeignKey.name}'


# Many to Many

class ExampleStore(models.Model):
    name =  models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    exampleVarieties = models.ManyToManyField(ModelExample,related_name="exampleStores")

    def __str__(self):
        return self.name


# One to One

class ExampleCertificate(models.Model):
    exampleCertificate = models.OneToOneField(ModelExample,on_delete=models.CASCADE,related_name="exampleCertificate")
    certificateNumber = models.CharField(max_length=100)
    issueDate = models.DateTimeField(default=timezone.now)
    validUntil = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.exampleCertificate.name}'