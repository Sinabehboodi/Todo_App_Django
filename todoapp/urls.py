from django.urls import path 

from . import views


app_name = 'todoapp'

urlpatterns = [
    path('', views.home_, name='todo_home'),
    path('list/', views.todo_list_view, name='todo_list'),
    path('create/', views.todo_item_create, name='create_todo_item'),
    path('delete/<int:pk>/', views.todo_item_delete, name='delete_todo_item'),
]

