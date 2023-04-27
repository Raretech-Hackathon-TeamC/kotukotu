from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import RegistForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

# Home画面
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


# ユーザー登録用
class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

# login用
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

# logout用
class UserLogoutView(LogoutView):
    pass