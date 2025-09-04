# from django.db import models

# Create your models here.

from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    assigned_courses = models.ManyToManyField("courses.Course", related_name="professors", blank=True)

    def __str__(self):
        return self.name
