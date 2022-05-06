from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Resets the kudos_left field for users"

    def handle(self, *args, **options):
        users = User.objects.all()
        users.update(kudos_left=3)

        for user in users:
            user.save()
        self.stdout.write("Kudos left for users were reset.")
