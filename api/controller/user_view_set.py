import logging

from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny

from application.service.user_application import UserApplication
from domain.models.user import User


class UserDeserializer(serializers.ModelSerializer):
    user_application = UserApplication()
    class Meta:
        model = User
        fields = ('username', 'password')
        #fields = ('name', 'description', 'cost')
    def create(self, validated_data: dict) -> User:
        return self.user_application.create_user(validated_data['username'], validated_data['password'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        #fields = ('name', 'description', 'cost')


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return UserSerializer
        return UserSerializer




