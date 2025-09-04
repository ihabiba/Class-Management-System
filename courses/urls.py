from django.urls import path
from .views import (
    CourseListCreateView,
    CourseDetailView,
    CourseUpdateView,
    CourseDeleteView,
)

urlpatterns = [
    path("", CourseListCreateView.as_view(), name="course-list-create"),        # http://127.0.0.1:8000/courses/
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),        # http://127.0.0.1:8000/courses/1/
    path("update/<int:pk>/", CourseUpdateView.as_view(), name="course-update"), # http://127.0.0.1:8000/courses/update/1/
    path("delete/<int:pk>/", CourseDeleteView.as_view(), name="course-delete"), # http://127.0.0.1:8000/courses/delete/1/
]
