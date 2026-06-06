from rest_framework.generics import ListAPIView
from apps.shop.models import Category 
from api.user.serializers.category_serializer import CategoryListSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

