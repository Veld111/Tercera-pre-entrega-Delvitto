# Generated by Django 4.2.5 on 2023-10-05 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppNotas", "0002_notasguardadas_rename_categoria_eliminarnota_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="crearnota",
            name="camada",
            field=models.IntegerField(default=0),
        ),
    ]