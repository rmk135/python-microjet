"""Profile domain models."""

from microjet import models


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()


class ProfilePasswordHasher:
    """Profile password hasher."""
