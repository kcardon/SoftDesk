from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (
    ProjectAPIView,
    ProjectUsersAPIView,
    ProjectIssuesAPIView,
    CommentAPIView,
)
from authentication.views import (
    UserAPIView,
    SignupAPIView,
    LoginAPIView,
)


"""SoftDesk_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/", include(router.urls)),
    path(
        "api/login/", LoginAPIView.as_view(), name="login"
    ),  # Ajoutez cette ligne pour le Login
]

# Création du routeur
router_root = routers.DefaultRouter()
# Déclaration des urls du routeur

router_root.register("signup", SignupAPIView, basename="users")
router_root.register("user", UserAPIView, basename="user")
router_root.register("projects", ProjectAPIView, basename="projects")
urlpatterns += [path("api/", include(router_root.urls))]

router_project = routers.DefaultRouter()
router_project.register("users", ProjectUsersAPIView, basename="projet_users")
router_project.register("issues", ProjectIssuesAPIView, basename="projet_users")
urlpatterns += [path("api/projects/<int:project_id>/", include(router_project.urls))]

router_issue = routers.DefaultRouter()
router_issue.register("comments", CommentAPIView, basename="comments")
urlpatterns += [
    path(
        "api/projects/<int:project_id>/issues/<int:issue_id>/",
        include(router_issue.urls),
    )
]
