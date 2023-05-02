from django.urls import path
from users.views import ( 
  RegistUserView, HomeView, UserLoginView, UserLogoutView
)

app_name = 'users'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('register/', RegistUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]