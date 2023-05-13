from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from users import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'get_users'})),
    path('users/create/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('users/create-token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('users/get-token/', views.UserViewSet.as_view({'get': 'get_user'})),


    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]