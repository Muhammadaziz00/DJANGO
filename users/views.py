from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from users.forms import UserRegistrationForm

class RegisterView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register-done')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password2'])
        new_user.save()
        return super().form_valid(form)
    
class RegisterDoneView(generic.TemplateView):
    template_name="registration/register_done.html"