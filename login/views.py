from django.contrib.auth import login, logout
from django.views.generic import RedirectView, FormView

from .forms import CadastroForm, UserForm


class Login(FormView):
    form_class = UserForm
    template_name = "login/login.html"
    success_url = "/games/"

    def form_valid(self, form):
        login(self.request, form.user)
        return super(Login, self).form_valid(form)


class Logout(RedirectView):
    pattern_name = "game:games"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class Cadastro(FormView):
    form_class = CadastroForm
    template_name = "login/cadastro.html"
    success_url = "/games/"

    def form_valid(self, form):
        new_user = form.save_user()
        login(self.request, new_user)
        return super().form_valid(form)
