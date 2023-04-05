from rest_framework.permissions import BasePermission
from .models import Contributor
from rest_framework.permissions import SAFE_METHODS


class IsContributor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés

        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
                and (
                    request.user.id == obj.author_user_id.id
                    or Contributor.objects.filter(
                        project_id=obj.id, user=request.user
                    ).exists()
                )
            )
        else:
            return bool(
                request.user
                and request.user.is_authenticated
                and request.user.id == obj.author_user.id
            )
