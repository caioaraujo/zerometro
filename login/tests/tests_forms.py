from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase

from ..forms import CadastroForm, UserForm


class TestForms(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Usuario1", password="123abc", email="aaa@123.com"
        )

    def test_user_form__success(self):
        form = UserForm(data={"usuario": "Usuario1", "senha": "123abc"})

        self.assertTrue(form.is_valid())

    def test_user_form__user_not_found(self):
        form = UserForm(data={"usuario": "usuario", "senha": "senha"})

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, "user_not_found"))

    def test_cadastro_form__clean_data__success(self):
        form = CadastroForm(
            data={
                "nome": "John",
                "sobrenome": "Lennon",
                "email": "john@lennon.com",
                "usuario": "j.lennon",
                "senha": "123abc",
                "senha2": "123abc",
            }
        )

        self.assertTrue(form.is_valid())

    def test_cadastro_form__email_already_exists(self):
        form = CadastroForm(
            data={
                "nome": "AAA",
                "email": "aaa@123.com",
                "usuario": "123abc",
                "senha": "123abc",
                "senha2": "123abc",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field="email", code="email_already_exists"))

    def test_cadastro_form__username_already_exists(self):
        form = CadastroForm(
            data={
                "nome": "AAA",
                "email": "usuer@123.com",
                "usuario": "Usuario1",
                "senha": "123abc",
                "senha2": "123abc",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field="usuario", code="username_already_exists"))

    def test_cadastro_form__passwords_not_match(self):
        form = CadastroForm(
            data={
                "nome": "AAA",
                "email": "usuer@123.com",
                "usuario": "Usuario2",
                "senha": "123abc",
                "senha2": "abc123",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, code="passwords_not_match"))

    def test_cadastro_form__save_user__success(self):
        form = CadastroForm(
            data={
                "nome": "John",
                "sobrenome": "Lennon",
                "email": "john@lennon.com",
                "usuario": "j.lennon",
                "senha": "123abc",
                "senha2": "123abc",
            }
        )
        self.assertTrue(form.is_valid())
        new_user = form.save_user()
        self.assertEqual("John", new_user.first_name)
        self.assertEqual("Lennon", new_user.last_name)
        self.assertEqual("john@lennon.com", new_user.email)
        # Assert password was saved encrypted
        self.assertTrue(new_user.password)
        self.assertNotEqual("123abc", new_user.password)
