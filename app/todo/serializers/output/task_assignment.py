from rest_framework import serializers
from todo.models import TaskAssignment
from todo.serializers.output.task import BaseTaskOutputSerializer
from todo.serializers.output.user import UserOutputSerializer

class TaskAssignmentOutputSerializer(serializers.ModelSerializer):
    task = BaseTaskOutputSerializer()
    user = UserOutputSerializer()

    class Meta:
        model = TaskAssignment
        fields = '__all__'