from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


# class ProfileEdit(forms.ModelForm):
#     first_name = forms.CharField(label='Имя')
#     last_name = forms.CharField(label='Фамилия')
#     email = forms.EmailField()
#
#     class Meta:
#         model = Profile
#         fields = ['about_me', 'date_of_birth']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'about_me']
