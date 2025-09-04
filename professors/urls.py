from django.urls import path
from .views import (
    ProfessorListCreateView,
    ProfessorDetailView,
    ProfessorUpdateView,
    ProfessorDeleteView,
)

urlpatterns = [
    path("", ProfessorListCreateView.as_view(), name="professor-list-create"),        # http://127.0.0.1:8000/professors/
    path("<int:pk>/", ProfessorDetailView.as_view(), name="professor-detail"),        # http://127.0.0.1:8000/professors/1/
    path("update/<int:pk>/", ProfessorUpdateView.as_view(), name="professor-update"), # http://127.0.0.1:8000/professors/update/1/
    path("delete/<int:pk>/", ProfessorDeleteView.as_view(), name="professor-delete"), # http://127.0.0.1:8000/professors/delete/1/
]
