from django.urls import path
from .views import (
    todo_list,
    todo_retrieve,
    todo_create,
    todo_update,
    todo_delete
)

app_name = 'todos'

urlpatterns = [
    path('todo_list/', todo_list),
    path('todo_list/create_todo', todo_create),
    path('todo_list/<id>/', todo_retrieve),
    path('todo_list/<id>/update_todo', todo_update),
    path('todo_list/<id>/delete_todo', todo_delete)
]
