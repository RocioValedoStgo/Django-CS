# from django.shortcuts import render

# # Create your views here.

# # -------------------------- MODELOS ---------------------
# from ejemplo.models import Profile

# # -------------------------- SERIALIZERS -------------------
# from ejemplo.serializer import EjemploSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework import status
# from django.http import Http404

# class ProfileList(APIView):
#     def get(self,request, format=None):
#         queryset = Profile.objects.filter(delete=False) #Retornar todo sin ninguna restriccion el All
#         #filter  bajo parametros. retorna si esta en falso
#         serializer = EjemploSerializer(queryset, many=True)#Control total -many-
#         return Response(serializer.data)