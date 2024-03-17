"""
Django wait command for the database be available
"""
import time

from psycopg2 import OperationalError as Pyscopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django wait command for the database"""

    def handle(self, *args, **options):
        """Entrypoint for commaned"""
        self.stdout.write('Waiting for database connection...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pyscopg2OpError, OperationalError):
                self.stdout.write('Database unavilable, waiting 1 second....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
