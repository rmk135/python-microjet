"""Auth domain models."""

from microjet import models

from .profile import Profile


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(Profile)
