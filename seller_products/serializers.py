from rest_framework import serializers
from products import serializers as product_serializer
from seller_products import models


class CreateSellerProductSerializer(serializers.ModelSerializer):
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.SellerProduct
        fields = (
            'seller',
            'product',
            'amount',
            'amount_currency',
            'is_active',
        )


class UpdateSellerProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SellerProduct
        fields = (
            'amount',
            'amount_currency',
            'is_active',
        )


class SellerProductSerializer(serializers.ModelSerializer):
    product = product_serializer.ProductSerializer()

    class Meta:
        model = models.SellerProduct
        fields = '__all__'
