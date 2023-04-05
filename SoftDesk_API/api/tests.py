from django.test import TestCase

# Create your tests here.
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from api.models import User, Contributor, Project, Issue, Comment


class TestUser(APITestCase):
    # Nous stockons l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans chacun de nos tests
    url = reverse_lazy("users-list")

    def test_list(self):
        # Créons deux catégories dont une seule est active
        user = User.objects.create(
            password="test21",
            username="test21",
            email="test21@test.com",
            first_name="test21",
            last_name="test21",
        )

        # On réalise l’appel en GET en utilisant le client de la classe de test
        response = self.client.get(self.url)
        print(response.json()["results"])
        # Nous vérifions que le status code est bien 200
        # et que les valeurs retournées sont bien celles attendues
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                "id": 1,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "email": user.email,
            }
        ]
        self.assertEqual(excepted, response.json()["results"])


# class TestProject(APITestCase):
#     # Nous stockons l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans chacun de nos tests
#     url = reverse_lazy("projects-list")

#     def test_list(self):
#         user = User.objects.create(
#             password="test",
#             username="test",
#             email="test",
#             first_name="test",
#             last_name="test",
#         )
#         project = Project.objects.create(
#             title="test_project",
#             description="Description test",
#             type="project",
#             author_user_id=User.objects.first(),
#         )

#         # On réalise l’appel en GET en utilisant le client de la classe de test
#         response = self.client.get(self.url)
#         # Nous vérifions que le status code est bien 200
#         # et que les valeurs retournées sont bien celles attendues
#         self.assertEqual(response.status_code, 200)
#         excepted = [
#             {
#                 "id": project.pk,
#                 "title": project.title,
#                 "description": project.description,
#                 "type": project.type,
#                 "author_user_id": {
#                     "id": user.pk,
#                     "username": user.username,
#                     "email": user.email,
#                     "first_name": user.first_name,
#                     "last_name": user.last_name,
#                 },
#             }
#         ]
#         self.assertEqual(excepted, response.json()["results"])
