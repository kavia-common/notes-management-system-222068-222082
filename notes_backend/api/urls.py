from django.urls import path
from .views import (
    health,
    NotesListCreateView,
    NotesRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("health/", health, name="Health"),
    # Notes CRUD endpoints
    path("notes/", NotesListCreateView.as_view(), name="notes-list-create"),
    path("notes/<int:pk>/", NotesRetrieveUpdateDestroyView.as_view(), name="notes-detail"),
]
