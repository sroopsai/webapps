from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def todo_list(request):
    return render(request, 'todo/todo_list.html')