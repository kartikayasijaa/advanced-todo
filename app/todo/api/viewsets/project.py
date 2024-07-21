from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from todo.serializers import input, output
from rest_framework.response import Response
from rest_framework import status
from todo.models import Project
        

class ListCreateProjectViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    input_serializer_class = input.CreateProjectInputSerializer
    output_serializer_class = output.ProjectOutputSerializer

    def list(self, request, *args, **kwargs):
        projects = Project.objects.filter(owner=request.user)
        output_serializer = self.output_serializer_class(projects, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
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
    
class UpdateDeleteRetrieveProjectViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    input_serializer_class = input.UpdateProjectInputSerializer
    output_serializer_class = output.ProjectOutputSerializer
    
    def patch(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs.get('id'))
        input_serializer = self.input_serializer_class(data=request.data, instance=project)
        input_serializer.is_valid(raise_exception=True)
        project.updated_by = request.user
        project.save()
        output_serializer = self.output_serializer_class(project)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs.get('id'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    