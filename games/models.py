from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    MIDIA_CHOICES = {
        "FISICA": "Física",
        "DIGITAL": "Digital",
    }

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, help_text="Nome do game")
    plataforma = models.ForeignKey(
        "Plataforma",
        related_name="games",
        related_query_name="game",
        on_delete=models.CASCADE,
        help_text="Plataforma",
    )
    midia = models.CharField(
        max_length=10,
        help_text="Tipo de mídia. Ex: física, digital",
        choices=MIDIA_CHOICES,
    )
    data_criado = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "game"
        ordering = ["nome", "plataforma"]
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.completado:
            self.finalizado = True
            self.lista_desejos = False
        if self.finalizado:
            self.lista_desejos = False
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    def __str__(self):
        if self.plataforma:
            return f"{self.nome} - {self.plataforma.nome}"
        return self.nome


class Plataforma(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=100, unique=True, help_text="Nome da plataforma. Ex: Playstation 2"
    )

    class Meta:
        db_table = "plataforma"
        ordering = ["nome"]
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"

    def __str__(self):
        return self.nome


class Progresso(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(
        "Game",
        related_name="game_progresso",
        related_query_name="game_progresso",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name="user_game_progresso",
        related_query_name="user_game_progresso",
        on_delete=models.CASCADE,
    )
    finalizado = models.BooleanField(help_text="Finalizado?")
    completado = models.BooleanField(
        help_text="Verdadeiro caso tenha obtido o set completo de conquistas/trofeus"
    )
    lista_desejos = models.BooleanField(help_text="Lista de desejos?")
    data_criado = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "progresso"
        ordering = ["game"]
        verbose_name = "Progresso"
        verbose_name_plural = "Progressos"
