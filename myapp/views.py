from django.shortcuts import render


from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Task, Project
from .serializers import TaskSerializer, ProjectSerializer
from .permissions import *
from rest_framework import viewsets, filters
from .models import Organization, Project, Task
from .serializers import OrganizationSerializer, ProjectSerializer, TaskSerializer
from .permissions import IsOrganizationMember

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, organization=self.request.user.organization)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'assigned_to', 'due_date']
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(organization=user.organization)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            organization=self.request.user.organization
        )

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.organization != request.user.organization:
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return Organization.objects.filter(id=self.request.user.organization.id)

