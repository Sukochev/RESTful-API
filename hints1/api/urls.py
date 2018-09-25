from .views import HintsRudView, HintsListApiView, HTMLAPIView
from . import views


from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets





urlpatterns = [
    url(r'^(?P<pk>\d+)$', HintsRudView.as_view(), name='hints-rud'),
    url(r'^$', HintsListApiView.as_view(), name='hints-list')  
]
