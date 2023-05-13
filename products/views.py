from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny

from products import models, serializers
from products.permissions import IsMe
from utils import mixins


# Create your views here.

class ProductViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsMe,)

    # def get_permissions(self):
    #     if self.action in SAFE_METHODS:
    #         return AllowAny(),
    #     return IsMe(),


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
