from django.urls import path
from todo.views import ListTodo

urlpatterns = [
    path('', ListTodo.as_view()),
]
