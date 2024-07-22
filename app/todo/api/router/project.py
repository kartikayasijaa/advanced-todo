from django.urls import path
from todo.api.viewsets.project import ProjectViewSet

urlpatterns = [
    path('project', ProjectViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='project-list-create'),
    path('project/<uuid:id>', ProjectViewSet.as_view({
        'delete': 'delete',
        'patch': 'update',
    }), name='project-update-delete'),
]