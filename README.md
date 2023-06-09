# SoftDesk

L'API Django Rest de SofDesk est créée dans le cadre d'un projet du parcours **Développeur d'application - Python** d'openclassrooms.

## Description

"SoftDesk, une société d'édition de logiciels de développement et de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B."

Les points de terminaison sont développés conformément au cahier des charges et en vue traitement des données par les applications des 3 plateformes (site web, applications Android et iOS). 

## Sécurité

La prévention des vulnérabilités auxquelles sont exposées les API a été prise en compte à travers le respect des recommandations de l'OWASP, notamment via le processus AAA (Authentication, Authorization, Accounting) des protocoles réseau.

- Authentication : Utilisation de tokens JWT
- Hachage de mot de passe : utilisation de la fonction Argon2
- Autorisation : Différentes règles restreignent l'accès des personnes non autorisés aux ressources exposées à travers les API.
- Accès : Les accès aux modifications et suppression des ressources sont également contraints selon le statut des utilisateurs identifiés.

## Configuration requise
- Python 3.x
- Django 3.x
### Fonctionnement de l'application en local.

L'application est lancée en local, sur un serveur de développement.

1. Créez un dossier dédié à l'application. 

2. Clônez le dépôt Git dans votre répertoire local:
`git clone https://github.com/kcardon/SoftDesk.git`

3. Créez et lancez un environnement virtuel:
`python -m venv env`
`.\env\Scripts\Activate.ps1`

4. Installez les dépendances prérequises:
`pip install requirements.txt`

5. Créez la base de données:
`python manage.py migrate`

6. Lancez l'application:
`cd SoftDesk_API`
`python manage.py runserver`

7. Utilisez la documentation POSTMAN pour effectuer les requêtes appropriées auprès des points de terminaison requis:
`https://documenter.getpostman.com/view/25029281/2s93XzyNay`

