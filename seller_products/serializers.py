from rest_framework import serializers
from products import serializers as product_serializer
from seller_products import models


class SellerProductSerializer(serializers.ModelSerializer):
    product = product_serializer.ProductSerializer()

    class Meta:
        model = models.SellerProduct
        fields = '__all__'
