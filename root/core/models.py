import uuid as uuid_lib

from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    """
    Abstract model that provides self updating
    `created` and `modified` fields
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract model that provides uuid field so that private information
    like the number of users isn't exposed through sequential ids
    """

    uuid = models.UUIDField(unique=True, default=uuid_lib.uuid4, editable=False)

    class Meta:
        abstract = True
