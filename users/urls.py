from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    # Auth endpoints
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # User management (staff only)
    path("", UserListView.as_view(), name="user-list"),                     # http://127.0.0.1:8000/auth/
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),        # http://127.0.0.1:8000/auth/3/
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user-update"), # http://127.0.0.1:8000/auth/update/3/
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"), # http://127.0.0.1:8000/auth/delete/3/
]
