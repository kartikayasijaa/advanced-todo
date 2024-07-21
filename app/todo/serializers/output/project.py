from rest_framework import serializers
from todo.models.project import Project
from todo.serializers.output.user import UserOutputSerializer

class ProjectOutputSerializer(serializers.ModelSerializer):
    owner = UserOutputSerializer()
    class Meta:
        model = Project
        fields = '__all__'