from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Note model with basic validation.
    Ensures title is present and not only whitespace.
    """

    # PUBLIC_INTERFACE
    def validate_title(self, value: str) -> str:
        """Validate that title is not empty or only whitespace."""
        if value is None:
            raise serializers.ValidationError("Title is required.")
        if not str(value).strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value.strip()

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
