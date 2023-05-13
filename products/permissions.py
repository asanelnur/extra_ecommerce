from rest_framework.permissions import DjangoObjectPermissions, SAFE_METHODS
from . import models


class IsMe(DjangoObjectPermissions):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.email == 'asd@gmail.com'
        )

    def has_object_permission(self, request, view, obj: models.Product):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

