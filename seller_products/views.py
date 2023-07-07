from django.shortcuts import render
from rest_framework import viewsets

from seller_products import models, serializers, permissions
from utils import mixins


# Create your views here.


class SellerProductViewSet(mixins.ActionSerializerMixin,
                           mixins.ActionPermissionMixin,
                           viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateSellerProductSerializer,
        'update': serializers.UpdateSellerProductSerializer,
        'partial_update': serializers.UpdateSellerProductSerializer,
    }
    ACTION_PERMISSIONS = {
        'update': (permissions.IsSellerAndOwner(),),
        'partial_update': (permissions.IsSellerAndOwner(),),
        'destroy': (permissions.IsSellerAndOwner(),),
    }
    queryset = models.SellerProduct.objects.select_related('seller', 'product')
    serializer_class = serializers.SellerProductSerializer
    permission_classes = permissions.IsSellerOrReadOnly,

