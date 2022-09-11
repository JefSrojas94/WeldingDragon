from django.urls import path
from WeldingDragonApp import Views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', Views.UserCreateView.as_view()),
    path('user/<int:pk>/', Views.UserDetailview.as_view())
]