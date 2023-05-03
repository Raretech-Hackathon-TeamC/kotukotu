from django.urls import path
from . import views

app_name = 'activity'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list/', views.ActivityListView.as_view(), name='activity_list'),
    path('add/', views.ActivityAddView.as_view(), name='activity_add'),
    path('<int:pk>/edit/', views.ActivityEditView.as_view(), name='activity_edit'),
    path('<int:pk>/delete/', views.ActivityDeleteView.as_view(), name='activity_delete'),
]

# TODO:ホーム(home)画面, 編集(edit)画面, 削除(delete)モーダルの作成
