from django.urls import path
from .views import TaskView, TaskDetailView, TaskCreateView

urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('task-detail/<slug>/', TaskDetailView.as_view(), name="detail"),
    path("task-create/", TaskCreateView.as_view(), name="task_create")

]