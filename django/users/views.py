from django.views.generic.edit import CreateView
from users.forms import RegistForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

# ユーザー登録用
class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm
    success_url = reverse_lazy('activity:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response

# login用
class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm


# logout用
class UserLogoutView(LogoutView):
    pass