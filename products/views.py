from django.shortcuts import render
from rest_framework import viewsets

from products import models, serializers
from utils import mixins


# Create your views here.

class ProductViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer



class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
