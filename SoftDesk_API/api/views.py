from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import User, Project, Contributor, Issue, Comment
from .serializers import (
    UserSerializer,
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

import logging

logger = logging.getLogger(__name__)


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
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.all()


class ProjectUsersAPIView(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Contributor.objects.filter(project_id=project_id)


class ProjectIssuesAPIView(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Issue.objects.filter(project_id=project_id)


class CommentAPIView(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        issue_id = self.kwargs["issue_id"]
        return Comment.objects.all()


"""     def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
