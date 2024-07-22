from rest_framework import serializers
from todo.models import Task
from todo.serializers.output.project import ProjectOutputSerializer

class BaseTaskOutputSerializer(serializers.ModelSerializer):
    end_date = serializers.DateField()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'start_date',
            'duration',
            'is_public',
            'is_completed',
            'end_date',
        ]


class TaskOutputSerializer(BaseTaskOutputSerializer):
    project = ProjectOutputSerializer()
    parent_task = serializers.SerializerMethodField()
    sub_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = BaseTaskOutputSerializer.Meta.fields + ['project', 'parent_task', 'sub_tasks']


    def get_parent_task(self, obj: Task):
        if obj.parent_task:
            return BaseTaskOutputSerializer(obj.parent_task).data
        return None

    def get_sub_tasks(self, obj: Task):
        sub_tasks = obj.sub_tasks.all()
        return BaseTaskOutputSerializer(sub_tasks, many=True).data
