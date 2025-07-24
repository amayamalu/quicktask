from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import TaskViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = router.urls
