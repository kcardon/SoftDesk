from django.db import models
from django.conf import settings
from authentication.models import User

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192)
    type = models.CharField(max_length=128)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Contributor(models.Model):
    # Table de relation entre un user et un projet
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class PermissionChoices(models.TextChoices):
        LEAD = "lead", "lead"
        CONTRIBUTOR = "contributor", "contributor"

    permission = models.CharField(max_length=15, choices=PermissionChoices.choices)
    role = models.CharField(max_length=128)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=8192)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=128)
    author_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="issues_created"
    )
    assignee_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="issues_assigned"
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.TextField(max_length=8192)
    author_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_created"
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
