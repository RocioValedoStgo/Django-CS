from django.urls import path,re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^$', views.EstudianteList.as_view()),
    re_path(r'^detalle/(?P<id>\d+)/$',views.EstudianteDetail.as_view()),
]
