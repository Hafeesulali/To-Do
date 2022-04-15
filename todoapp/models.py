from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todos(models.Model):
    task_name = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name
