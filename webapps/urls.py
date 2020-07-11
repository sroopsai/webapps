
from django.contrib import admin
from django.urls import path
from todo.views import todo_list

urlpatterns = [
    path('todo_list/', todo_list),
    path('admin/', admin.site.urls),
]
