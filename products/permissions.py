from rest_framework.permissions import DjangoObjectPermissions, SAFE_METHODS
from . import models


class IsAdminOrReadOnly(DjangoObjectPermissions):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )

