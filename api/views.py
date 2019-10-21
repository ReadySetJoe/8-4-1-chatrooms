from django.shortcuts import render
from django.views import generic
from rest_framework import generics

from todos.models import Todo
from .serializers import TodoSerializer

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
