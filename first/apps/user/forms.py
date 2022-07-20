from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=250,
        label="Имя пользователя",
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ("username", "password")


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=250,
        label="Имя",
    )
    last_name = forms.CharField(
        max_length=250,
        label="Фамилия",
    )
    email = forms.EmailField(
        label="E-mail",
    )
    username = forms.CharField(
        max_length=250,
        label="Имя пользователя",
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
