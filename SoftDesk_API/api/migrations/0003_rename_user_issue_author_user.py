# Generated by Django 4.1.7 on 2023-04-03 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="issue",
            old_name="user",
            new_name="author_user",
        ),
    ]
