from rest_framework.permissions import BasePermission
from .models import Contributor, Project, Issue, Comment
from rest_framework.permissions import SAFE_METHODS


class IsContributor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # On récupère l'objet projet pour accéder plus tard à la liste de ses contributeurs.
        if isinstance(obj, Project):
            project = obj
        elif isinstance(obj, Issue):
            project = obj.project
        elif isinstance(obj, Comment):
            project = obj.issue.project
        elif isinstance(obj, Contributor):
            obj = project = obj.project

        # Les objets associés à un projet sont visibles par leur auteur
        # ainsi que par tous les contributeurs au projet.
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and (
                    request.user.id == project.author_user.id
                    or Contributor.objects.filter(
                        project_id=project.id, user=request.user
                    ).exists()
                )
            )
        else:
            # La modification et suppression n'est autorisée qu'aux auteurs de l'objet (project, issue, comment)
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user.id == obj.author_user.id
            )
