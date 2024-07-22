from django.urls import path
from todo.api.viewsets.task_assignment import TaskAssignmentViewSet

urlpatterns = [
    path('task_assignment', TaskAssignmentViewSet.as_view({
        'post': 'add_assignee',
        'delete': 'remove_assignee',
    }), name='task-assigment')
]