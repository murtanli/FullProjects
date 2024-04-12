from django import forms
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    login = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

class UserRegistrationForm(forms.ModelForm):
    login = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Почта'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ['login', 'email', 'password']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['login']  # Устанавливаем значение username равным значению login
        if commit:
            user.save()
        return user