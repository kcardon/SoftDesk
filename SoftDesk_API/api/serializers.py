from rest_framework.serializers import ModelSerializer
from .models import User, Project, Contributor, Issue, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ProjectSerializer(ModelSerializer):
    author_user_id = UserSerializer()

    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user_id"]


class ContributorSerializer(ModelSerializer):
    user = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "permission", "role"]


class IssueSerializer(ModelSerializer):
    user = UserSerializer()
    assignee_user = UserSerializer()

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
            "user",
            "assignee_user",
            "created_time",
        ]


class CommentSerializer(ModelSerializer):
    author_user = UserSerializer()

    class Meta:
        model = Comment
        fields = ["id", "description", "author_user", "issue", "created_time"]
