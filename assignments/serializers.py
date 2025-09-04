from rest_framework import serializers
from .models import Assignment
from courses.models import Course

class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "code")

class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseMiniSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        write_only=True,
        source="course"
    )

    class Meta:
        model = Assignment
        fields = ("id", "title", "description", "date", "course", "course_id")
