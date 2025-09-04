# from django.db import models

# Create your models here.

from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="assignments")

    def __str__(self):
        return f"{self.title} ({self.course.code})"
