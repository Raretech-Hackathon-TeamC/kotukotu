from django.views.generic.edit import CreateView
from users.forms import RegistForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView

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