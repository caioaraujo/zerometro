# Generated by Django 5.0.6 on 2024-09-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_add_related_name_for_plataforma"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="lista_desejos",
            field=models.BooleanField(default=False, help_text="Lista de desejos?"),
            preserve_default=False,
        ),
    ]
