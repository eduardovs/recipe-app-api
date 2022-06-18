"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """django command to wait for database to be ready"""

    def handle(self, *args, **options):
        pass
