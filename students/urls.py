from django.urls import path
from .views import (
    StudentListCreateView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path("", StudentListCreateView.as_view(), name="student-list-create"),        # http://127.0.0.1:8000/students/ (list & create)
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),        # http://127.0.0.1:8000/students/1/ (detail)
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="student-update"), # http://127.0.0.1:8000/students/update/1/ (update)
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"), # http://127.0.0.1:8000/students/delete/1/ (delete)
]
