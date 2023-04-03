from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        unique=True
    )  # Assurez-vous que le champ e-mail est unique
    groups = models.ManyToManyField(Group, related_name="users_in_group")
    user_permissions = models.ManyToManyField(
        Permission, related_name="users_with_permission"
    )
