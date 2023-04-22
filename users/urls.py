from django.urls import path
from .views import RegisterView, RegisterDoneView

urlpatterns = [
    path("users/register/", RegisterView.as_view(), name = "register"),
    path("users/register/done/", RegisterDoneView.as_view(), name='register-done')
]