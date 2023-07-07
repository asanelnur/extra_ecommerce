from django.shortcuts import render
from rest_framework.response import Response

from utils import mixins
from . import models, serializers, services
from rest_framework import viewsets, status


# Create your views here.


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.OrderItem.objects.all()


class OrderViewSet(mixins.ActionSerializerMixin, viewsets.ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateOrderSerializer,
    }
    order_services: services.OrderServicesInterface = services.OrderServicesV1()
    queryset = order_services.get_orders()
    serializer_class = serializers.OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.order_services.create_order(serializer.validated_data)
        data = serializers.OrderSerializer(order).data
        return Response(data, status=status.HTTP_201_CREATED)


