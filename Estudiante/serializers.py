# ----------------------------- Librerias -----------------------------
from rest_framework import routers, serializers, viewsets

from drf_dynamic_fields import DynamicFieldsMixin

# ----------------------------- Modelos -----------------------------
from Estudiante.models import Estudiante

class EstudianteSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id','name','lastname','age','gender','subject','address','phoneNumber','birthday','enrollment','profesorId')