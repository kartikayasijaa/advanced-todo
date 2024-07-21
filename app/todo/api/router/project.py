from django.urls import path
from todo.api.viewsets.project import ListCreateProjectViewSet, UpdateDeleteRetrieveProjectViewSet

urlpatterns = [
    path('project', ListCreateProjectViewSet.as_view(), name='project-list-create'),
    path('project/<uuid:id>', UpdateDeleteRetrieveProjectViewSet.as_view(), name='project-update-delete-retrieve'),
]