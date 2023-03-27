from rest_framework import routers
from django.urls import include, path
from django.contrib import admin

from api.views import (
    UserAPIView,
    ProjectAPIView,
    ContributorAPIView,
    IssueAPIView,
    CommentAPIView,
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
# Création du routeur
router = routers.SimpleRouter()
# Déclaration des urls du routeur
router.register("users", UserAPIView, basename="users")
router.register("projects", ProjectAPIView, basename="projects")
router.register("contributors", ContributorAPIView, basename="contributors")
router.register("issues", IssueAPIView, basename="issues")
router.register("comments", CommentAPIView, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
]
