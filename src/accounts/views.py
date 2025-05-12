from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('cars_list')


class UserLogoutView(LogoutView):
    next_page = 'login'
