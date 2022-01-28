from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_absolute_url(self):
        return reverse_lazy("tasks")


class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "main/task_list.html"
    context_object_name = "tasks"

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Task.objects.filter(user=user)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     context['count'] = context['tasks'].filter(completed=False).count()
    #     return context

def UserTaskView(self, request):
    task = Task.objects.filter(user=self.request.user)
    user = User.objects.filter(username=self.request.user.username)
    context = {
        "task": task,
        "user": user,
    }
    return render(request, "main/new.html", context)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "main/task_detail.html"
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'slug']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)
        

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'slug']


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/"




    