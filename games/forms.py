from django import forms


class GameForm(forms.Form):
    finalizado = forms.BooleanField()
    completado = forms.BooleanField()
    lista_desejos = forms.BooleanField()
