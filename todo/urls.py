from django.urls import path
from todo.views import ListCreateTodo, UpdateDeleteTodo

urlpatterns = [
    path('', ListCreateTodo.as_view()),
    path('<int:todo_id>/', UpdateDeleteTodo.as_view())
]
