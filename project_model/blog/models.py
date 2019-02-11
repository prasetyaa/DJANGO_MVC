from django.db.models import TextField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.
from django.db import models as models

class Mentee(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.TextField(max_length=255)
    gender = models.CharField(max_length=1)
    telephone = models.TextField(max_length=25)
    mobile = models.TextField(max_length=25)
    address = models.TextField(max_length=255)
    nick_name = models.TextField(max_length=10)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    posted_by = models.ForeignKey(Mentee, on_delete= models.CASCADE)
