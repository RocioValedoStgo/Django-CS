from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from User.models import User

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    phoneNumber = models.IntegerField(null=False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'User'
