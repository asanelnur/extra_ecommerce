from django.shortcuts import render
from rest_framework import viewsets

from seller_products import models, serializers


# Create your views here.


class SellerProductViewSet(viewsets.ModelViewSet):
    queryset = models.SellerProduct.objects.select_related('seller', 'product')
    serializer_class = serializers.SellerProductSerializer
