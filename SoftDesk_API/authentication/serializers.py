from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    ValidationError,
    EmailField,
    CharField,
)
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password

from .models import User
import logging

logger = logging.getLogger(__name__)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Cet email est déjà enregistré")
        return value

    def create(self, validated_data):
        password = validated_data["password"]
        hashed_password = make_password(password)
        user = User.objects.create_user(
            # L'adresse email est utilisée comme username
            username=validated_data["email"],
            email=validated_data["email"],
            password=hashed_password,
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user


class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        print(f"Email: {email}")
        print(f"Password: {password}")
        user = User.objects.get(email=email)
        if user is None:
            raise ValidationError("A user with this email and password is not found.")
        if check_password(password, user.password):
            print("Le mot de passe est correct.")
            user = authenticate(username=email, password=password)
            print(f"Authenticated user: {user}")
        else:
            print("Le mot de passe est incorrect")
        data["user"] = user
        return data
