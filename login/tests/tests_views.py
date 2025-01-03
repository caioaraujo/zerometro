from django.contrib import auth
from django.contrib.auth import get_user_model
from django.test import TestCase

class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Usuario1", password="123abc"
        )

    def test_login__success(self):
        response = self.client.post(
            "/login.html", {"usuario": "Usuario1", "senha": "123abc"}
        )

        self.assertRedirects(response, "/games/", status_code=302)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get("/logout", follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/games/")
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_cadastro__success(self):
        data = {
            "nome": "Test123",
            "sobrenome": "Silva",
            "email": "teste@123.com",
            "usuario": "Usuario2",
            "senha": "123abc",
            "senha2": "123abc",
        }
        response = self.client.post("/cadastro.html", data)

        self.assertRedirects(response, "/games/", status_code=302)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
