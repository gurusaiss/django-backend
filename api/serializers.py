from rest_framework import serializers
from django.contrib.auth.models import User

class PublicSerializer(serializers.Serializer):
    message = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
