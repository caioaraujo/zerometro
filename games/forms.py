from django import forms


class GameForm(forms.Form):
    finalizado = forms.BooleanField(required=False)
    completado = forms.BooleanField(required=False)
    lista_desejos = forms.BooleanField(required=False)
