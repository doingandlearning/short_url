from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL

class Command(BaseCommand):
    help = 'Refreshes all shortcodes'

    def handle(self, *args, **options):
        print(options)
        return ShortURL.objects.refresh_shortcodes()