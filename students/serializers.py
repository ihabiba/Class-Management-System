from rest_framework import serializers
from .models import Student
from courses.models import Course

class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "code")

class StudentSerializer(serializers.ModelSerializer):
    # show enrolled courses (read-only)
    enrolled_courses = CourseMiniSerializer(many=True, read_only=True)
    # accept course IDs when creating/updating (write-only)
    course_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        write_only=True,
        source="enrolled_courses"
    )

    class Meta:
        model = Student
        fields = ("id", "name", "email", "enrolled_courses", "course_ids")
