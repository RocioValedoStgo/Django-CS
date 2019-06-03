# ------------Librerias------------
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Profile.models import Profile
# ----------------serializers-------------
from Profile.serializers import ProfileSerializers

# ------------------LIBRERIAS EXTERNAS------------------
# import json

class ProfileList(APIView):
    # METODO PARA EXPLICITAR LA INFORMACION
    def get(self, request, format=None):
        queryset = Profile.objects.filter(delete = False)
        serializer = ProfileSerializers(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    # METODO PARA CREAR NUEVO REGISTRO 
    def post(self, request, format=None):
        serializer = ProfileSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    #METODO PARA COSULTAR ID Y E RETORNE SI EXISTE O NO
    # def get_object(self,pk):
    #     try: 
    #         return Profile.objects.get(pk=pk)
    #     except Profile.DoesNotExist:
    #         return "No"

    def get_object(self, id):
        try:
            return Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return 404

    def get(self, request,id, format=None):
        profile = self.get_object(id) 
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)

    #METODO PARA CONSULTAR ID Y DEVOLVER LOS VALORES DE SUS CAMPOS 
    # def get(self, request,pk, format=None):
    #     print("Este es el id:"+pk)
    #     Id = self.get_object(pk) 
    #     if Id != "No":
    #         Id = ProfileSerializers(Id)
    #         return Response(Id.data)
    #     return Response("No existe")
    #METODO CONSULTAR ID Y ACTUALIZAR DATOS 
    def put(self, request,pk, format=None):
        Id = self.get_object(pk)
        serializer = ProfileSerializers(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response("Error", status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
   parser_class = (FileUploadParser,)
   def post(self, request, *args, **kwargs):
      file_serializer = ProfileSerializer(data=request.data)
      if file_serializer.is_valid():
         file_serializer.save()
         return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  