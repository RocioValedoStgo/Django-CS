# ----------------------------- Librerias -----------------------------
from rest_framework import routers, serializers, viewsets

from drf_dynamic_fields import DynamicFieldsMixin

# ----------------------------- Modelos -----------------------------
from Modulo.models import Modulo

class ModuloSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ('id','num_esp32','mac_esp32', 'idUser')
