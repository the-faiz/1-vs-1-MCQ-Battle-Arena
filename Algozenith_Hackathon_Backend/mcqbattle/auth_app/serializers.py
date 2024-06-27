from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        max_length=30,
        required=True,
        error_messages={
            "required": "First Name is required",
            "blank": "First Name is required",
        }
    )
    last_name = serializers.CharField(
        max_length=30,
        required=True,
        error_messages={
            "required": "Last Name is required",
            "blank": "Last Name is required",
        }
    )
    email = serializers.EmailField(
        required=True,
        error_messages={
            "required": "Email is required",
            "blank": "Email is required",
            "invalid": "Enter a valid email address",
        }
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            "required": "Password is required",
            "blank": "Password is required",
        }
    )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        error_messages={
            "required": "Email is required",
            "blank": "Email is required",
            "invalid": "Enter a valid email address",
        }
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        error_messages={
            "required": "Password is required",
            "blank": "Password is required",
        }
    )

#My serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'created_at', 'updated_at', 'is_active', 'is_staff', 'is_superuser']

