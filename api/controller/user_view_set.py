from rest_framework import viewsets, serializers

from domain.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



