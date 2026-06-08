from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.order.models import Order 
from api.user.serializers.order_serializer import OrderListSerializer, OrderCreateSerializer



class OrderListApiView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateApiView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
