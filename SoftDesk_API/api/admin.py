from django.contrib import admin
from api.models import User, Project, Contributor, Issue, Comment

# Register your models here.

for model in [User, Project, Contributor, Issue, Comment]:
    admin.site.register(model)
