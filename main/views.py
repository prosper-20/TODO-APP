from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_absolute_url(self):
        return reverse_lazy("tasks")


class TaskView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/"




    