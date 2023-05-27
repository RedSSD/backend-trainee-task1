from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserView(APIView):

    def get(self, request, user_id):

        user = CustomUser.objects.get(user_id=user_id)
        serialized_user = CustomUserSerializer(user)
        return JsonResponse(serialized_user.data)


class FundsAccuralView(APIView):

    def put(self, request, user_id, amount):

        user = CustomUser.objects.get(user_id=user_id)

        if not user.funds_accural(amount):
            return HttpResponse('REQUEST ERROR')

        return redirect(f'/user/{user_id}')


class FundsDebitView(APIView):

    def put(self, request, user_id, amount):

        user = CustomUser.objects.get(user_id=user_id)

        if not user.funds_debit(amount):
            return HttpResponse('REQUEST ERROR')

        return redirect(f'/user/{user_id}')
