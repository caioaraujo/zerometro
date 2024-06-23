from django.db import models


class Game(models.Model):
    MIDIA_CHOICES = {
        "FISICA": "Física",
        "DIGITAL": "Digital",
    }

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, help_text="Nome do game")
    plataforma = models.ForeignKey(
        "Plataforma",
        related_name="plataforma",
        on_delete=models.CASCADE,
        help_text="Plataforma",
    )
    finalizado = models.BooleanField(help_text="Finalizado?")
    completado = models.BooleanField(
        help_text="Verdadeiro caso tenha obtido o set completo de conquistas/trofeus"
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
