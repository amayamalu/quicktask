from django.shortcuts import render


from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'assigned_to', 'due_date']
    ordering_fields = ['due_date', 'created_at']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()  
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]