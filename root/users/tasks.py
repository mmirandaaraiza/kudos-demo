from celery.schedules import crontab
from django.contrib.auth import get_user_model
from django.core.management import call_command

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0, day_of_week="monday"),
        reset_kudos_left.s(),
    )


@celery_app.task
def reset_kudos_left():
    call_command("reset_kudos_left")
