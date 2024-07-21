from typing import Any
from django.db import models
from todo.models.user import User
from app.mixins import TimeStampModelMixin
import uuid

class Project(TimeStampModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='projects', null=True)
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_projects', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_projects', null=True)
