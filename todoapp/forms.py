from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from todoapp.models import Todos


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
            "username",
            "password1",
            "password2"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"})
        }


class LoginFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = [
            "task_name"
        ]
        widgets = {
            "task_name": forms.TextInput(attrs={"class": "form-control"})
        }


class TodoChangeForm(TodoForm):
    class Meta:
        model = Todos
        fields = [
            "task_name",
            "completed"
        ]
        widgets = {
            "task_name": forms.TextInput(attrs={"class": "form-control"}),
        }
