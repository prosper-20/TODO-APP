from django.urls import path
from .views import (
    TaskView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CustomLoginView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', TaskView.as_view(), name="home"),
    path("user/<str:username>/", TaskView.as_view(), name="home"),
    path('task-detail/<slug>/', TaskDetailView.as_view(), name="detail"),
    path("task-create/", TaskCreateView.as_view(), name="create"),
    path("task-update/<slug>/", TaskUpdateView.as_view(), name="update"),
    path("task-delete/<slug>/", TaskDeleteView.as_view(), name="delete"),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name='logout'),


]