from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task


class TaskView(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"

class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"

class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"




    