from django.db.models import Min, Q, Count
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny

from products import models, serializers, services
from products.permissions import IsAdminOrReadOnly
from utils import mixins


# Create your views here.

class ProductViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    product_services: services.ProductServicesInterface = services.ProductServicesV1()
    queryset = product_services.get_products()
    serializer_class = serializers.ProductSerializer
    permission_classes = IsAdminOrReadOnly,


class ProductImageViewSet(viewsets.ModelViewSet):
    product_image_services: services.ProductImageServicesInterface = services.ProductImageServicesV1()
    queryset = product_image_services.get_product_images()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = IsAdminOrReadOnly,
