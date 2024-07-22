from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.serializers import input, output
from rest_framework.response import Response
from rest_framework import status
from todo.models import Project
from django.shortcuts import get_object_or_404
        

class ProjectViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    input_serializer_class = input.ProjectInputSerializer
    output_serializer_class = output.ProjectOutputSerializer

    def list(self, request, *args, **kwargs):
        projects = Project.objects.filter(owner=request.user)
        output_serializer = self.output_serializer_class(projects, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        input_serializer = self.input_serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        project = Project.objects.create(
            owner=request.user,
            created_by=request.user,
            updated_by=request.user,
            **input_serializer.validated_data
        )
        output_serializer = self.output_serializer_class(project)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        try:
            project = Project.objects.get(id=kwargs.get('id', None))
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

        if project.created_by != request.user:
            return Response({'error': 'You are not allowed to update this Project'}, status=status.HTTP_403_FORBIDDEN)

        input_serializer = self.input_serializer_class(project, data=request.data, partial=True)
        input_serializer.is_valid(raise_exception=True)

        try:
            project.update(**input_serializer.validated_data, updated_by=request.user)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        output_serializer = self.output_serializer_class(project)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
    

    def delete(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs.get('id'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    