from django.urls import path

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.Games.as_view(), name="games"),
]
