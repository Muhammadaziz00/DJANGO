from django.shortcuts import render
from django.views import View
from users.forms import UserRegistrationForm

class RegisterView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, "registration/register.html", {'form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {'form': user_form})