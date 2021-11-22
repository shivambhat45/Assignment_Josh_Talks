from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework import viewsets

# Create your views here.
from AppApi.serializers import VideoInfoSerializer
from AppApi.models import VideoInfo


from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


#Defining what the view you wanted also applying some filters like ordering,searching

class Output(generics.ListAPIView):
    search_fields=['title','description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    ordering_fields=['publishedDateTime']
    queryset = VideoInfo.objects.all()
    serializer_class=VideoInfoSerializer
