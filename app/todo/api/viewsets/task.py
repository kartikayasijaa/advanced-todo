from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.serializers import input, output
from todo.models import Task, Project
from rest_framework.response import Response
from rest_framework import status


class TaskViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    input_serializer_class = input.TaskInputSerializer
    output_serializer_class = output.TaskOutputSerializer

    def list(self, request):
        tasks = Task.objects.filter(created_by=request.user, parent_task=None)
        output_serializer = self.output_serializer_class(tasks, many=True)
        return Response(output_serializer.data)

    def create(self, request):
        input_serializer = self.input_serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        project = input_serializer.validated_data.get('project')

        if project.owner != request.user:
            return Response({'error': 'You are not allowed to create task for this project'}, status=status.HTTP_403_FORBIDDEN)
        
        task = Task.objects.create(
            created_by=request.user,
            updated_by=request.user,
            **input_serializer.validated_data
        )

        output_serializer = self.output_serializer_class(task)
        return Response(output_serializer.data)
    
    def update(self, request, *args, **kwargs):
        try:
            task = Task.objects.get(id=kwargs.get('id', None))
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        input_serializer = self.input_serializer_class(task, data=request.data, partial=True)
        input_serializer.is_valid(raise_exception=True)

        try:
            task.update(**input_serializer.validated_data, user=request.user)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        output_serializer = self.output_serializer_class(task)
        return Response(output_serializer.data, status=status.HTTP_200_OK)

    
    def delete(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs.get('id', None))
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
