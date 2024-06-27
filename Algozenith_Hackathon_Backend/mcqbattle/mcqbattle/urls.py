# urls.py
from django.contrib import admin
from django.urls import path

from auth_app.views import LoginView, ProtectedView, RegisterView, UserListView
from mcqs.views import MCQListCreateView, MCQRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("protected", ProtectedView.as_view(), name="protected"),
    path("mcqs", MCQListCreateView.as_view(), name="mcq-list-create"),
    path("mcqs/<uuid:pk>", MCQRetrieveUpdateDestroyView.as_view(), name="mcq-detail"),
    path('users/', UserListView.as_view(), name='user-list'),
]
