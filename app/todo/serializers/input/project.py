from rest_framework import serializers
import datetime

class CreateProjectInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=500, required=False)
    start_date = serializers.DateField()
    is_public = serializers.BooleanField(default=True)
    owner = serializers.UUIDField(required=False)

    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")
        return value
    
class UpdateProjectInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(max_length=500, required=False)
    start_date = serializers.DateField(required=False)
    is_public = serializers.BooleanField(required=False)
    owner = serializers.UUIDField(required=False)

    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")
        return value
