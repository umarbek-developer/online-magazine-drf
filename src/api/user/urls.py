from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views.category_view import CategoryListApiView
from api.user.views.product_view import ProductListApiView


router = DefaultRouter()
router.include_root_view = False

urlpatterns = [

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),

    path('product/', ProductListApiView.as_view()),
    path('category/', CategoryListApiView.as_view()),
]
