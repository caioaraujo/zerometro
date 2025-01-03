# Generated by Django 5.1.4 on 2025-01-03 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [
        ("games", "0001_initial"),
        ("games", "0002_add_related_name_for_plataforma"),
        ("games", "0003_add_game_lista_desejos"),
        ("games", "0004_add_progresso"),
        ("games", "0005_remove_game_completado_remove_game_finalizado_and_more"),
    ]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Plataforma",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nome",
                    models.CharField(
                        help_text="Nome da plataforma. Ex: Playstation 2",
                        max_length=100,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Plataforma",
                "verbose_name_plural": "Plataformas",
                "db_table": "plataforma",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(help_text="Nome do game", max_length=250)),
                (
                    "midia",
                    models.CharField(
                        choices=[("FISICA", "Física"), ("DIGITAL", "Digital")],
                        help_text="Tipo de mídia. Ex: física, digital",
                        max_length=10,
                    ),
                ),
                ("data_criado", models.DateTimeField(auto_now_add=True)),
                ("data_alterado", models.DateTimeField(auto_now=True)),
                (
                    "plataforma",
                    models.ForeignKey(
                        help_text="Plataforma",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        related_query_name="game",
                        to="games.plataforma",
                    ),
                ),
            ],
            options={
                "verbose_name": "Game",
                "verbose_name_plural": "Games",
                "db_table": "game",
                "ordering": ["nome", "plataforma"],
            },
        ),
        migrations.CreateModel(
            name="Progresso",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("finalizado", models.BooleanField(help_text="Finalizado?")),
                (
                    "completado",
                    models.BooleanField(
                        help_text="Verdadeiro caso tenha obtido o set completo de conquistas/trofeus"
                    ),
                ),
                ("lista_desejos", models.BooleanField(help_text="Lista de desejos?")),
                ("data_criado", models.DateTimeField(auto_now_add=True)),
                ("data_alterado", models.DateTimeField(auto_now=True)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="game_progresso",
                        related_query_name="game_progresso",
                        to="games.game",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_game_progresso",
                        related_query_name="user_game_progresso",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Progresso",
                "verbose_name_plural": "Progressos",
                "db_table": "progresso",
                "ordering": ["game"],
            },
        ),
    ]