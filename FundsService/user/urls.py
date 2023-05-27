from django.contrib import admin
from django.urls import path, include
from .views import CustomUserView, FundsAccuralView, FundsDebitView


urlpatterns = [
    path('<int:user_id>/', CustomUserView.as_view()),
    path('<int:user_id>/accural/<str:amount>', FundsAccuralView.as_view()),
    path('<int:user_id>/debit/<str:amount>', FundsDebitView.as_view()),
]
