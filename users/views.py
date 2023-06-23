from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from users import serializers, services, models


# Create your views here.


class UserViewSet(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()
    # permission_classes = (IsAuthenticated,)

    def get_users(self, request, *args, **kwargs):
        users = models.CustomUser.objects.all()
        serializer = serializers.CreateUserSerializer(users, many=True)
        return Response(serializer.data)

    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        self.user_services.create_user(data=serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create_token(self, request, *args, **kwargs):
        serializer = serializers.CreateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = self.user_services.create_token(data=serializer.validated_data)

        return Response(tokens)

    def get_user(self, request, *args, **kwargs):
        serializer = serializers.GetUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = Token.objects.get(key=serializer.validated_data['token'])
        return Response({
            'email': token.user.email
        })
