from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def health(request):
    """
    Health endpoint to verify the server is running.
    Returns HTTP 200 with a simple JSON message.
    """
    return Response({"message": "Server is up!"}, status=status.HTTP_200_OK)


class NotesListCreateView(generics.ListCreateAPIView):
    """
    GET /notes/ -> List all notes
    POST /notes/ -> Create a new note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]


class NotesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /notes/{id}/ -> Retrieve a single note
    PUT/PATCH /notes/{id}/ -> Update a note
    DELETE /notes/{id}/ -> Delete a note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        """
        Override to return 404 if not found using get_object_or_404 for clarity.
        """
        return get_object_or_404(Note, pk=self.kwargs.get("pk"))
