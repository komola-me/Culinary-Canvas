from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from recipes.models import Recipe


class Command(BaseCommand):
    help = "Publish old draft recipes that are older than a given number of days"

    def add_arguments(self, parser):
        parser.add_argument(
            "--days",
            type=int,
            default=30,
            help="Number of days to check for old drafts (default: 30 days)",
        )

    def handle(self, *args, **options):
        days = options["days"]
        cutoff_date = timezone.now() - timedelta(days=days)

        old_drafts = Recipe.objects.filter(is_draft=True, created_at__lt=cutoff_date)

        count = old_drafts.update(is_draft=False)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully published {count} old draft(s) older than {days} days."
            )
        )
