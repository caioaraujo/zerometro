from django.contrib import admin

from .models import Game


class MyAdminSite(admin.AdminSite):
    site_header = "Zerometro administration"


class GameAdmin(admin.ModelAdmin):
    list_display = ["nome", "plataforma", "finalizado"]
    list_filter = ["nome", "plataforma", "finalizado"]
    search_fields = ["nome"]


admin_site = MyAdminSite(name="admin")
admin_site.register(Game, GameAdmin)
