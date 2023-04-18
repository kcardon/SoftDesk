from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .permissions import IsContributor
from .models import User, Project, Contributor, Issue, Comment
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    """ def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


class ProjectAPIView(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsContributor,)

    def get_queryset(self):
        return Project.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            "message": "Project has been deleted",
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class ProjectUsersAPIView(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = (IsContributor,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project_id=project_id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            "message": "Contributor has been deleted",
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class ProjectIssuesAPIView(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (IsContributor,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Issue.objects.filter(project_id=project_id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            "message": "Issue has been deleted",
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class CommentAPIView(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsContributor,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        issue_id = self.kwargs["issue_id"]
        return Comment.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            "message": "Comment has been deleted",
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
