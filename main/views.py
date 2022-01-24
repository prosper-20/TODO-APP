from django.shortcuts import render
from django.views.generic import ListView
from .models import Task


class TaskView(ListView):
    model = Task
