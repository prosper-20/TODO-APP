from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task


class TaskView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "main"
    