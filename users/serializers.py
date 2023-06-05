from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from .models import CustomUser


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = CustomUser.USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password')

    def save(self):
        user = CustomUser.objects.create_user(**self.validated_data)