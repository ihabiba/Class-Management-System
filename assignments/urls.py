from django.urls import path
from .views import (
    AssignmentListCreateView,
    AssignmentDetailView,
    AssignmentUpdateView,
    AssignmentDeleteView,
)

urlpatterns = [
    path("", AssignmentListCreateView.as_view(), name="assignment-list-create"),
    # GET  http://127.0.0.1:8000/assignments/   -> list all assignments
    # POST http://127.0.0.1:8000/assignments/   -> create new assignment (staff only if you want)


    path("<int:pk>/", AssignmentDetailView.as_view(), name="assignment-detail"),
    # GET  http://127.0.0.1:8000/assignments/1/ -> retrieve assignment with id=1

    path("update/<int:pk>/", AssignmentUpdateView.as_view(), name="assignment-update"),
    # PUT  http://127.0.0.1:8000/assignments/update/1/ -> update assignment with id=1 (staff only)

    path("delete/<int:pk>/", AssignmentDeleteView.as_view(), name="assignment-delete"),
    # DELETE http://127.0.0.1:8000/assignments/delete/1/ -> delete assignment with id=1 (staff only)

]
