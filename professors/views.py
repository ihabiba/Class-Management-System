# from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStaff
from .models import Professor
from .serializers import ProfessorSerializer

# List all professors / create new
class ProfessorListCreateView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

# Retrieve single professor
class ProfessorDetailView(generics.RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

# Update professor (staff only)
class ProfessorUpdateView(generics.UpdateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsStaff]

# Delete professor (staff only)
class ProfessorDeleteView(generics.DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsStaff]
