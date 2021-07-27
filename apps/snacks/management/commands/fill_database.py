from django.core.management.base import BaseCommand
from apps.snacks.fill_database import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Filling the database...")
        try:
            main()
            self.stdout.write("Database Filled.")
        except TypeError:
            self.stdout.write("A problem occured during the process.")
