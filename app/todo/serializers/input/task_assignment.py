from rest_framework import serializers
from todo.models import Task, User

class TaskAssignmentInputSerializer(serializers.Serializer):
    task = serializers.UUIDField(required=True)
    user = serializers.UUIDField(required=True)

    def validate_task(self, value):
        try:
            return Task.objects.get(id=value)
        except Task.DoesNotExist:
            raise serializers.ValidationError("Task not found.")
        
    def validate_user(self, value):
        try:
            return User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")