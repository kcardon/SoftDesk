from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    ValidationError,
    EmailField,
    CharField,
    PrimaryKeyRelatedField,
)
from django.contrib.auth import authenticate
from .models import User, Project, Contributor, Issue, Comment
import logging


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ProjectSerializer(ModelSerializer):
    author_user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user"]


class ContributorSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]


class IssueSerializer(ModelSerializer):
    author_user = PrimaryKeyRelatedField(queryset=User.objects.all())
    assignee_user = PrimaryKeyRelatedField(queryset=User.objects.all())
    project = PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "desc",
            "tag",
            "priority",
            "project",
            "status",
            "author_user",
            "assignee_user",
            "created_time",
        ]


class CommentSerializer(ModelSerializer):
    author_user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "description", "author_user", "issue", "created_time"]
