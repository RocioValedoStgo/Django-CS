from django.urls import path,re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
#from Profile import views

from django.conf import settings
from . import views

urlpatterns=[
   re_path(r'^$', views.ProfileList.as_view()),
   re_path(r'^lista/$', views.ProfileList.as_view()), #estaba comentada
   re_path(r'^detalle/(?P<id>\d+)/$',views.ProfileDetail.as_view()),
   #re_path(r'^/(?P<pk>\d+)/$',views.ProfileDetail.as_view()),
   re_path(r'^img/$',views.FileUploadView.as_view()),
]