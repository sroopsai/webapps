from django.shortcuts import render

from todo.models import Todo


# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos_list": todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_retrieve(request, id):
    todo = Todo.objects.get(id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)
