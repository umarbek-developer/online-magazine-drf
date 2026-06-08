from rest_framework.generics import ListAPIView
from apps.order.models import Order 
from api.user.serializers.order_serializer import OrderListSerializer


class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

