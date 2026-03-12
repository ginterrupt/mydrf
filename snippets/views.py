#snippet/view.py

#from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer

class SnipetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer