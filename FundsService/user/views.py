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

    def put(self, request):

        amount = request.query_params.get('amount')
        user_id = int(request.query_params.get('id'))
        user = CustomUser.objects.get(user_id=user_id)

        if not user.funds_accural(amount):
            return HttpResponse('REQUEST ERROR')

        return redirect(f'/user/{user_id}')


class FundsDebitView(APIView):

    def put(self, request):

        amount = request.query_params.get('amount')
        user_id = int(request.query_params.get('id'))
        user = CustomUser.objects.get(user_id=user_id)

        if not user.funds_debit(amount):
            return HttpResponse('REQUEST ERROR')

        return redirect(f'/user/{user_id}')


class FundsSendView(APIView):

    def put(self, request):

        amount = request.query_params.get('amount')
        user_id = int(request.query_params.get('id'))
        receiver_id = int(request.query_params.get('receiver'))
        user = CustomUser.objects.get(user_id=user_id)
        receiver = CustomUser.objects.get(user_id=receiver_id)

        if not user.funds_debit(amount):
            return HttpResponse('REQUEST ERROR')

        receiver.funds_accural(amount)
        return redirect(f'http://127.0.0.1:8000/user/{receiver_id}')

