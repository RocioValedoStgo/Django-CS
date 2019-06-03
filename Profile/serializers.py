# ----------------LIBRERIAS-----------------
from rest_framework import routers, serializers, viewsets
from drf_dynamic_fields import DynamicFieldsMixin

# -----------------MODELOS-------------------
     #Nombre App                 Nombre modelo
from Profile.models import Profile

class ProfileSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'address')
        #fields = ('id','name','ap_pat','ap_mat','year','img')

        