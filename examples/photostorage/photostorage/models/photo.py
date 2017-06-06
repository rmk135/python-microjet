"""Photo domain models."""

from microjet import models

from .profile import Profile


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(Profile)
