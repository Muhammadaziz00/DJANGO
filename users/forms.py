from django.contrib.auth.models import User
from django import forms

class UserReqistrationForm(forms.ModelsForm):
    password = forms.CharField(laabel = "Пароль", widget = forms.PasswordIput)
    password2 = forms.CharField(lable = "Повторите пароль", widget = forms.PasswordInput)


    class Meta:
        model = User
        fiels = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_date
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароль не совподает!")
        return cd["password2"]

