from django.contrib import admin

from .models import Game, Plataforma, Progresso


class MyAdminSite(admin.AdminSite):
    site_header = "Zerometro administration"


class ProgressoAdmin(admin.ModelAdmin):
    list_display = ["user", "game", "finalizado", "completado", "lista_desejos"]
    list_filter = ["user"]
    search_fields = ["game__nome"]


class GameAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "plataforma",
    ]
    list_filter = [
        "nome",
        "plataforma",
    ]
    search_fields = ["nome"]


class PlataformaAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]


admin_site = MyAdminSite(name="admin")
admin_site.register(Game, GameAdmin)
admin_site.register(Plataforma, PlataformaAdmin)
admin_site.register(Progresso, ProgressoAdmin)
