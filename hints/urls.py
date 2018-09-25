"""hints URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from hints1.api.views import HTMLAPIView
from hints1.api import views





urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/hints/', include(('hints1.api.urls', 'api'), namespace='api-hints1')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', HTMLAPIView.as_view({'get': 'list'}), name='html' ),
]

# The last url allows the user to navigate to my custom HTML view. Also a Django REST Framework breadcrumb gets created in the DFR html.