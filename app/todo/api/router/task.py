from django.urls import path
from todo.api.viewsets.task import TaskViewSet

urlpatterns = [
    path('task', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='task-list-create'),
    path('task/<uuid:id>', TaskViewSet.as_view({
        'delete': 'delete',
        'patch': 'update'
    }), name='task-update-delete'),
]