# accounts/urls.py
from django.urls import path
from django.contrib.auth import views

from .views import SignUpView
from .forms import UserLoginForm

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name="registration/login.html", authentication_form=UserLoginForm),
         name="login"),
    path('signup/', SignUpView.as_view(),
         name='signup'),
]
