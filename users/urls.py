from django.urls import path

from .views import (
    UserRegisterAPIView,
    EmailConfirmAPIView,
    )

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name="register"),
    path('register/confirm/<str:token>/', EmailConfirmAPIView.as_view(), name="register-confirm"),
]
