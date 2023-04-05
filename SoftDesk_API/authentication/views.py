from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import (
    UserSerializer,
    SignUpSerializer,
    # LoginSerializer,
)

import logging

logger = logging.getLogger(__name__)


# Create your views here.
class UserAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class SignupAPIView(ModelViewSet):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginAPIView(APIView):
#     serializer_class = LoginSerializer
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]
#             # À ce stade, vous pouvez générer un token JWT, un token DRF ou utiliser une autre méthode d'authentification.
#             # Ici, nous renvoyons simplement l'email de l'utilisateur comme exemple.
#             return Response({"email": user.email}, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
