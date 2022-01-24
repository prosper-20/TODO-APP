from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="task")


    def __str__(self):
        return self.title 

    class Meta:
        ordering = ["completed"]