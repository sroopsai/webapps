from django.shortcuts import render, redirect
from .forms import TodoForm
from todo.models import Todo


# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todos_list": todos
    }
    return render(request, "todo/todo_list.html", context)


def todo_retrieve(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_retrieve.html", context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {"form": form}
    return render(request, "todo/todo_create.html", context)
