# from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStaff, IsProfessor  
from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework.exceptions import PermissionDenied



# List / create assignments
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            # Only staff or professors can create assignments
            permissions = [IsStaff(), IsProfessor()]
            for permission in permissions:
                if permission.has_permission(self.request, self):
                    return permissions
            raise PermissionDenied("You must be a staff or professor to create assignments")
        
        # Any logged-in user (students, professors, staff) can list assignments
        return [IsAuthenticated()]

# Retrieve single assignment
class AssignmentDetailView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

# Update assignment (staff only)
class AssignmentUpdateView(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    def get_permissions(self):
        permissions = [IsStaff(), IsProfessor()]
        for permission in permissions:
            if permission.has_permission(self.request, self):
                return permissions
        raise PermissionDenied("You must be a staff or professor to update assignments")
        
    # permission_classes = [IsStaff(), IsProfessor()]  # Or just leave this if you want it checked in all scenarios.


# Delete assignment (staff only)
class AssignmentDeleteView(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    def get_permissions(self):
        permissions = [IsStaff(), IsProfessor()]
        for permission in permissions:
            if permission.has_permission(self.request, self):
                return permissions
        raise PermissionDenied("You must be a staff or professor to delete assignments")