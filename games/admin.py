from django.contrib import admin

from .models import Game, Plataforma


class MyAdminSite(admin.AdminSite):
    site_header = "Zerometro administration"


class GameAdmin(admin.ModelAdmin):
    list_display = ["nome", "plataforma", "finalizado", "completado", "midia"]
    list_filter = ["nome", "plataforma", "finalizado", "completado", "midia"]
    search_fields = ["nome"]


class PlataformaAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]


admin_site = MyAdminSite(name="admin")
admin_site.register(Game, GameAdmin)
admin_site.register(Plataforma, PlataformaAdmin)
