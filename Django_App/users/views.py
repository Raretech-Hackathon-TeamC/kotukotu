from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from users.forms import RegistForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError

# Home画面
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


# ユーザー登録用
class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

# login用
class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm


# logout用
class UserLogoutView(LogoutView):
    pass