from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from api.controller.user_view_set import UserSerializer
from domain.models import User
from domain.models.review import Review


# ▶ 조회용 Serializer
class ReviewReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'comment', 'user']

# ▶ 생성/수정용 Serializer
class ReviewWriteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = ['comment', 'user_id']

        
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ReviewWriteSerializer
        return ReviewReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 🔹 인증된 사용자 자동 지정
