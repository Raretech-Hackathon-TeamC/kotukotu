from django.urls import path
from . import views

app_name = 'categories'

#TODO
urlpatterns = [
    path('add/', views.CategoryAddView.as_view(), name='category_add'),
    path('check_duplicate/', views.check_duplicate, name='check_duplicate'),
    path('restore/<int:pk>/', views.category_restore, name='category_restore'),
]
