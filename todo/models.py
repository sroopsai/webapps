from django.db import models


# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=120)
    due_time = models.TimeField()
    due_date = models.DateField()

    def __str__(self):
        return self.name
