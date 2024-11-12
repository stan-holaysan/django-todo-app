from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:todo_id>/todo_done/', views.todo_done, name='todo_done'),  
]