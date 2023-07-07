from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()

router.register(r'orders', views.OrderViewSet, basename='orders')
router.register(r'order-items', views.OrderItemViewSet, basename='order-items')
urlpatterns = router.urls
