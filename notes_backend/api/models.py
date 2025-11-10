from django.db import models


class Note(models.Model):
    """
    Note model representing a simple note with title and optional content.
    Includes created_at and updated_at timestamps.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = ("-updated_at", "-created_at")

    def __str__(self) -> str:
        return f"{self.title[:50]}"

