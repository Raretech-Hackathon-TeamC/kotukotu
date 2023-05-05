from django.urls import path
from users.views import ( 
    # TODO:HomeViewはactivityアプリを作成した後に削除
  RegistUserView, UserLoginView, UserLogoutView
)

app_name = 'users'

urlpatterns = [
    path('register/', RegistUserView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]