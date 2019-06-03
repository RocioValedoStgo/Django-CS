from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profesor(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=100, null=False) #Genero
    subject = models.CharField(max_length=100, null=False)
    yearsExperience = models.IntegerField(null=False)
    phoneNumber = models.IntegerField(null=False)
    birthday = models.DateField(default = timezone.now)
    #delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    #edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Profesor'
