from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from User.models import User

# Create your models here.

class Modulo(models.Model):
    idUser = models.ForeignKey(User, on_delete = models.SET(-1))
    num_esp32 = models.IntegerField(null=False)
    #date_now = models.DateTimeField(default = timezone.now)
    mac_esp32 = models.CharField(max_length=100, null=False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'Modulo'
