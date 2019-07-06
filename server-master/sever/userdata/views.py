from django.shortcuts import render
from rest_framework import generics
from userdata.serializers import DataSerializer

# Create your views here.
class DataCreate(generics.CreateAPIView):
    serializer_class = DataSerializer