# from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField("courses.Course", related_name="students", blank=True)

    def __str__(self):
        return self.name

