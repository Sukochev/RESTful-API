from rest_framework import generics, mixins
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from hints1.models import Hints
from .serializers import HintsSerializer, HTMLSerializer

from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

#Created a seperate custom HTML view using TemplateHTMLRenderer and HTMLSerializer

class HTMLAPIView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend.html'
    serializer_class = HTMLSerializer
    

    def list(self, request):
        queryset = Hints.objects.order_by('pk')
        paginator = Paginator(queryset, 5) # Show 5 items per page
        page = request.GET.get('page')
        queryset1 = paginator.get_page(page)
            
        return Response({'queryset1': queryset1})

    
""" This is the Django REST List View. Allows user to view all Hints as a list but in the Django REST Framework,
preprogrammed html view rather that my custom HTML API view. """

class HintsListApiView(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field = 'pk'
    serializer_class = HintsSerializer
    
    def get_queryset(self):
        qs = Hints.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(text__icontains=query)|
                Q(author__icontains=query)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    

''' This allows the user to view an individual Hint in the Django REST Framework preprogrammed html view.
And change it if they have the admin permission'''

class HintsRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'pk'
    serializer_class = HintsSerializer
    
    def get_queryset(self):
        return Hints.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


