from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskListCreate(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['completed','priority']

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer