from rest_framework import serializers
from .models import Professor
from courses.models import Course

class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "code")

class ProfessorSerializer(serializers.ModelSerializer):
    # show assigned courses (read-only)
    assigned_courses = CourseMiniSerializer(many=True, read_only=True)
    # accept course IDs for create/update
    course_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Course.objects.all(),
        write_only=True,
        source="assigned_courses"
    )

    class Meta:
        model = Professor
        fields = ("id", "name", "email", "assigned_courses", "course_ids")
