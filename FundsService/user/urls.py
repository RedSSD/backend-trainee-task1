from django.contrib import admin
from django.urls import path, include
from .views import CustomUserView


urlpatterns = [
    path('<int:user_id>/', CustomUserView.as_view())
]
