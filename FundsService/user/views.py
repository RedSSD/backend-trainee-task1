from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserView(APIView):

    def get(self, request, user_id):
        user = CustomUser.objects.get(user_id=user_id)
        serialized_user = CustomUserSerializer(user)
        return JsonResponse(serialized_user.data)
