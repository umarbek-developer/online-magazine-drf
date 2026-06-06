from rest_framework.generics import ListAPIView
from apps.shop.models import Product 
from api.user.serializers.product_serializer import ProductListSerializer



class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get("category_id")
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset
