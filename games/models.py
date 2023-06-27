from django.db import models


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, help_text="Nome do game")
    plataforma = models.CharField(max_length=100, help_text="Plataforma")
    finalizado = models.BooleanField(help_text="Finalizado?")
    data_criado = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "game"
        ordering = ["-id"]
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return f"{self.nome} - {self.plataforma}"
