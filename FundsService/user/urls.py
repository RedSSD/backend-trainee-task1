from django.contrib import admin
from django.urls import path, include
from .views import CustomUserView, FundsAccuralView, FundsDebitView


urlpatterns = [
    path('<int:user_id>/', CustomUserView.as_view()),
    path('accural/', FundsAccuralView.as_view()),
    path('debit/', FundsDebitView.as_view()),
]
