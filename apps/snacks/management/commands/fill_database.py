"""Custom command module."""


from django.core.management.base import BaseCommand
from apps.snacks.fill_database import main


class Command(BaseCommand):
    """Custom command."""

    def handle(self, *args, **options):
        """Call main function of fill_database module."""
        self.stdout.write("Filling the database...")
        try:
            main()
            self.stdout.write("Database Filled.")
        except TypeError:
            self.stdout.write("A problem occured during the process.")
