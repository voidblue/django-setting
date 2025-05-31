from rest_framework import viewsets, serializers

from domain.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')

        
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



