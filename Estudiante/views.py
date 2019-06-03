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
from Estudiante.models import Estudiante

# ----------------------------- Serializers -----------------------------
from Estudiante.serializers import EstudianteSerializers

# Create your views here.

class EstudianteList(APIView):
    # METODO PARA SOLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Estudiante.objects.all()   
        serializer = EstudianteSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)

    # METODO PARA CREAR NUEVO REGISTRO
    def post(self, request, format=None):
        serializer = EstudianteSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class EstudianteDetail(APIView):
    # METODO CONSULTAR EL ID Y ME RETORNE SI EXISTE O NO
    def get_object(self, id):
        try:
            return Estudiante.objects.get(pk=id)
        except Estudiante.DoesNotExist:
            return "No"

    # METODO CONSULTAR EL ID Y DEVOLVER LOS VALORES DE SUS CAMPOS
    def get(self, request, id, format=None):
        estudiante = self.get_object(id)
        serializer = EstudianteSerializers(estudiante)
        return Response(serializer.data)
    
    # METODO CONSULTAR EL ID Y ACTULIZAR LOS VALORES DE SUS CAMPOS
    def put(self, request, id, format=None):
        estudiante = self.get_object(id)
        serializer = EstudianteSerializers(estudiante, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #METODO DE ELIMINACION
    def delete(self, request, id, format=None):
        estudiante = self.get_object(id)
        estudiante.delete()
        return Response('Elemento Eliminado')
    

