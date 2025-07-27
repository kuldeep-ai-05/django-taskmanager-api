from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class TaskListCreate(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['completed','priority']
    permission_classes=[IsAuthenticated]

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer