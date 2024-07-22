from rest_framework import serializers
from todo.models.user import User

class CreateUserInputSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=False, max_length=10, min_length=10, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, min_length=5)
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return value

class LoginUserInputSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, min_length=5)
    
    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email does not exist.")
        return value