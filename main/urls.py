from django.urls import path
from .views import TaskView, TaskDetailView

urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('task-detail/<str:slug>/', TaskDetailView.as_view(), name="detail")

]