from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import (
    ProjectPermission,
    ProjectUserPermission,
    IssuePermission,
    CommentPermission,
)
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)


class ProjectAPIView(ModelViewSet):
    """return a list of projects
    access to a specific project is enabled for author or contributors only
    updating or deleting a specific project is enabled for author only"""

    serializer_class = ProjectSerializer
    permission_classes = (ProjectPermission,)

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
    """return the list of contributors to a specific project
    adding a new contributor is enabled for author and contributors to the project
    deleting a contributor is enabled for author of the contributor only"""

    serializer_class = ContributorSerializer
    permission_classes = (ProjectUserPermission,)

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
    """return the list of issues related to a specific project
    access to the list is limited to author and contributors to the project
    updating and deleting a specific issue is enabled for its author only"""

    serializer_class = IssueSerializer
    permission_classes = (IssuePermission,)

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
    """return a list of comments related to a specific issue
    access to this list is limited to the author and the contributors to the project
    updating and deleting a comment is enabled for its author only"""

    serializer_class = CommentSerializer
    permission_classes = (CommentPermission,)

    def get_queryset(self):
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
