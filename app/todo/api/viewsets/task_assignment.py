from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.serializers import input, output
from todo.models import TaskAssignment
from rest_framework.response import Response
from rest_framework import status
from todo.models import Task

class TaskAssignmentViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    input_serializer_class = input.TaskAssignmentInputSerializer
    output_serializer_class = output.TaskAssignmentOutputSerializer

    def add_assignee(self, request, *args, **kwargs):
        input_serializer = self.input_serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        task = Task.objects.get(id=input_serializer.validated_data.get('task'))
        if task.created_by != request.user:
            return Response({'error': 'You are not allowed to add assignee for this task'}, status=status.HTTP_403_FORBIDDEN)

        task_assignment = TaskAssignment.objects.create(
            created_by=request.user,
            updated_by=request.user,
            **input_serializer.validated_data
        )

        output_serializer = self.output_serializer_class(task_assignment)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def remove_assignee(self, request, *args, **kwargs):
        input_serializer = self.input_serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        task = Task.objects.get(id=input_serializer.validated_data.get('task'))
        if task.created_by != request.user:
            return Response({'error': 'You are not allowed to remove assignee for this task'}, status=status.HTTP_403_FORBIDDEN)

        try:
            task_assignment = TaskAssignment.objects.get(
                **input_serializer.validated_data
            )
            task_assignment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TaskAssignment.DoesNotExist:
            return Response({"detail": "TaskAssignment not found."}, status=status.HTTP_404_NOT_FOUND)


