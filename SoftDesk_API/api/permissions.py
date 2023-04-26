from rest_framework.permissions import BasePermission
from .models import Contributor, Project, Issue, Comment
from rest_framework.permissions import SAFE_METHODS


# class IsContributor(BasePermission):
#     """general permission allow any authenticated user to access to the get methods
#     object permission :
#     - safe methods applied to a specific object are enabled for their author or any contributor to the root project
#     - other methods applied to this specific object (as updating and deleting the object)
#     are enabled for their author only.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)

#     def has_object_permission(self, request, view, obj):
#         # On récupère l'objet projet pour accéder plus tard à la liste de ses contributeurs.
#         if isinstance(obj, Project):
#             project = obj
#         elif isinstance(obj, Issue):
#             project = obj.project
#         elif isinstance(obj, Comment):
#             project = obj.issue.project
#         elif isinstance(obj, Contributor):
#             obj = project = obj.project

#         # Les objets associés à un projet sont visibles par leur auteur
#         # ainsi que par tous les contributeurs au projet.
#         if request.method in SAFE_METHODS:
#             return bool(
#                 request.user
#                 and request.user.is_authenticated
#                 and (
#                     request.user.id == project.author_user.id
#                     or Contributor.objects.filter(
#                         project_id=project.id, user=request.user
#                     ).exists()
#                 )
#             )
#         else:
#             # La modification et suppression n'est autorisée qu'aux auteurs de l'objet (project, issue, comment)
#             return bool(
#                 request.user
#                 and request.user.is_authenticated
#                 and request.user.id == obj.author_user.id
#             )


class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return self.can_create_project(request)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return self.can_view_project(request, obj)
        return self.can_update_project(request, obj)

    def can_create_project(self, request):
        return bool(request.user and request.user.is_authenticated)

    def can_view_project(self, request, project):
        return bool(
            request.user
            and request.user.is_authenticated
            and (
                request.user == project.author_user
                or Contributor.objects.filter(
                    project=project, user=request.user
                ).exists()
            )
        )

    def can_update_project(self, request, project):
        return bool(
            request.user.is_authenticated and request.user == project.author_user
        )


class ProjectUserPermission(BasePermission):
    def get_project(self, view):
        project = Project.objects.get(id=view.kwargs.get("project_id"))
        return project

    def has_permission(self, request, view):
        return self.is_contributor(request, view)

    def has_object_permission(self, request, view, obj):
        return self.is_contributor(request, view)

    def is_contributor(self, request, view):
        project = self.get_project(view)
        return bool(
            request.user
            and request.user.is_authenticated
            and (
                request.user == project.author_user
                or Contributor.objects.filter(
                    project=project, user=request.user
                ).exists()
            )
        )


class IssuePermission(BasePermission):
    def get_project(self, view):
        project = Project.objects.get(id=view.kwargs.get("project_id"))
        return project

    def has_permission(self, request, view):
        return self.is_contributor(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return self.is_contributor(request, view)
        return self.is_author(request, view, obj)

    def is_contributor(self, request, view):
        project = self.get_project(view)
        print(project)
        return bool(
            request.user
            and request.user.is_authenticated
            and (
                request.user == project.author_user
                or Contributor.objects.filter(
                    project=project, user=request.user
                ).exists()
            )
        )

    def is_author(self, request, view, obj):
        return bool(request.user.is_authenticated and request.user == obj.author_user)


class CommentPermission(BasePermission):
    def get_project(self, view):
        project = Project.objects.get(id=view.kwargs.get("project_id"))
        return project

    def has_permission(self, request, view):
        return self.is_contributor(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return self.is_contributor(request, view)
        return self.is_author(request, view, obj)

    def is_contributor(self, request, view):
        project = self.get_project(view)
        return bool(
            request.user
            and request.user.is_authenticated
            and (
                request.user == project.author_user
                or Contributor.objects.filter(
                    project=project, user=request.user
                ).exists()
            )
        )

    def is_author(self, request, view, obj):
        return bool(request.user.is_authenticated and request.user == obj.author_user)
