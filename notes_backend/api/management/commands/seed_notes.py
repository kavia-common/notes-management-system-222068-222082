from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Seed the database with sample notes for testing."

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Create a few example notes."""
        samples = [
            {"title": "Welcome", "content": "This is your first note."},
            {"title": "Second Note", "content": "Feel free to edit or delete me."},
            {"title": "Ideas", "content": "Capture your ideas here."},
        ]
        created_count = 0
        for data in samples:
            obj, created = Note.objects.get_or_create(title=data["title"], defaults={"content": data["content"]})
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created_count} new notes."))
