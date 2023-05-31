from django.contrib import admin
from django.urls import path, include
from .views import CustomUserView, FundsAccuralView, FundsDebitView, FundsSendView


urlpatterns = [
    path('', CustomUserView.as_view()),
    path('accural/', FundsAccuralView.as_view()),
    path('debit/', FundsDebitView.as_view()),
    path('send/', FundsSendView.as_view()),
]
