from django.conf import settings
from django.db import models

from root.core.models import TimeStampedModel, UUIDModel


# Create your models here.
class Organization(TimeStampedModel, UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Kudos(TimeStampedModel, UUIDModel):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver"
    )
