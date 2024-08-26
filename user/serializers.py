from . import models
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    """user register serializer"""
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """validate attributes is valid or not"""
        print('attrs: ', attrs)
        return attrs

    def create(self, validated_data):
        user = models.User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'].lower(),
            contact_number=validated_data['contact_number'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = models.User
        fields = ["id", "name", "email", "contact_number", "password"]


class UserLoginSerializer(serializers.ModelSerializer):
    """user login serializer"""
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = models.User
        fields = ["email", "password"]
