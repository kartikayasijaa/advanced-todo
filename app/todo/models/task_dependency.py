from app.mixins import TimeStampModelMixin
from django.db import models
import uuid
from todo.models import User, Task
from todo.constants import AND, TASK_DEPENDENCY_CONDITION_CHOICES

class TaskDependency(TimeStampModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, related_name='dependencies', on_delete=models.CASCADE)
    depends_on = models.ForeignKey(Task, related_name='dependent_tasks', on_delete=models.CASCADE)
    condition = models.CharField(choices=TASK_DEPENDENCY_CONDITION_CHOICES, default=AND)
    created_by = models.ForeignKey(User, related_name='created_task_dependencies', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name='updated_task_dependencies', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['task', 'depends_on'], name='unique_task_dependency'),
        ]

    def save(self, *args, **kwargs):
        if self.task.project != self.depends_on.project:
            raise ValueError("Tasks must belong to the same project to have dependencies.")
        super().save(*args, **kwargs)
