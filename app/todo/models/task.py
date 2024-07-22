from app.mixins import TimeStampModelMixin
from django.db import models
import uuid
from todo.models import Project, User
from datetime import timedelta
from django.db import transaction
from django.core.exceptions import PermissionDenied

class Task(TimeStampModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.IntegerField()
    is_public = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_tasks', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_tasks', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_tasks', null=True)

    @property
    def end_date(self):
        return self.start_date + timedelta(days=self.duration)
    
    def update(self, user, **kwargs):
        with transaction.atomic():
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    if attr == 'is_completed':
                        if user != self.created_by and not self.assignments.filter(user=user).exists():
                            raise ValueError("Only the creator or an assignee can mark this task as completed.")

                        all_subtasks_completed = all(sub_task.is_completed for sub_task in self.sub_tasks.all())
                        if not all_subtasks_completed:
                            raise ValueError("Cannot mark task as completed when not all sub-tasks are completed.")
                        self.is_completed = True
                    else:
                        setattr(self, attr, value)
                else:
                    raise AttributeError(f"Attribute '{attr}' does not exist on Task model.")
            self.updated_by = user
            self.save()
