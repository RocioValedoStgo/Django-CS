# ----------------------------- Librerias -----------------------------
from rest_framework import routers, serializers, viewsets

from drf_dynamic_fields import DynamicFieldsMixin

# ----------------------------- Modelos -----------------------------
from User.models import User

class UserSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','lastname', 'subject', 'phoneNumber')
