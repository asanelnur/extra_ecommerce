from rest_framework import serializers

from users import models


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('email', 'password')



class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()
