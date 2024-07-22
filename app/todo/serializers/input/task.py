from rest_framework import serializers
import datetime
from todo.models import Task, Project

class TaskInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, required=False)
    start_date = serializers.DateField()
    duration = serializers.IntegerField(min_value=1)
    is_public = serializers.BooleanField(default=True)
    is_completed = serializers.BooleanField(default=False)
    parent_task = serializers.UUIDField(required=False)
    project = serializers.UUIDField(required=True)

    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")
        return value
    
    def validate_project(self, value):
        try:
            return Project.objects.get(id=value)
        except Project.DoesNotExist:
            raise serializers.ValidationError("Project not found.")
    
    def validate_parent_task(self, value):
        try:
            return Task.objects.get(id=value)
        except Task.DoesNotExist:
            raise serializers.ValidationError("Parent task not found.")