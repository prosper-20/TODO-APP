from django.urls import path
from .views import (
    TaskView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('task-detail/<slug>/', TaskDetailView.as_view(), name="detail"),
    path("task-create/", TaskCreateView.as_view(), name="create"),
    # path("task-update/<slug>/", TaskUpdateView.as_view(), name="update"),
    # path("task-delete/<slug>/", TaskDeleteView.as_view(), name="delete")


]