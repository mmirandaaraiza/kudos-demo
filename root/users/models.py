from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from root.core.models import TimeStampedModel, UUIDModel
from root.kudos.models import Organization


class User(TimeStampedModel, UUIDModel, AbstractUser):
    """
    Default custom user model for Kudos.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    kudos_left = models.PositiveSmallIntegerField(
        default=3, validators=[MaxValueValidator(3)]
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"uuid": self.uuid})
