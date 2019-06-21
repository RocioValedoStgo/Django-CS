#-----------------------LIBRERIAS-----------------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#----------------------- Modelos -----------------------
    #Nombre de la App           Nombre del modelo
from Modulo.models import Modulo

# ----------------------------- Serializers -----------------------------
from Modulo.serializers import ModuloSerializers

# Create your views here.

class ModuloList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Modulo.objects.filter(delete=True)   
        serializer = ModuloSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = ModuloSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class ModuloDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Modulo.objects.get(pk=id)
        except Modulo.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        modulo = self.get_object(id)
        serializer = ModuloSerializers(modulo)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        modulo = self.get_object(id)
        serializer = ModuloSerializers(modulo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        modulo = self.get_object(id)
        serializer = ModuloSerializers(modulo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

