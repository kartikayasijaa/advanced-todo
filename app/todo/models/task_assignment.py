from app.mixins import TimeStampModelMixin
from django.db import models
import uuid
from todo.models import User, Task

class TaskAssignment(TimeStampModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, related_name='assignments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='task_assignments', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_task_assignments', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name='updated_task_assignments', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['task', 'user'], name='unique_task_user')
        ]
