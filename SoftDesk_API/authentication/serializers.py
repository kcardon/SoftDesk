from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    ValidationError,
    EmailField,
    CharField,
)
from django.contrib.auth import authenticate, get_user_model
from .models import User
import logging

logger = logging.getLogger(__name__)


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Cet email est déjà enregistré")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            # L'adresse email est utilisée comme username
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
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
        logger.debug(f"Email: {email}")
        logger.debug(f"Password: {password}")
        user = authenticate(email=email, password=password)
        logger.debug(f"Authenticated user: {user}")

        if user is None:
            raise ValidationError("A user with this email and password is not found.")

        data["user"] = user
        return data