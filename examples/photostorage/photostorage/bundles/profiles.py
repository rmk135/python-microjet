"""Profiles bundle."""

from microjet import models


class ProfileService:
    """Profile service."""

    def __init__(self, profile_model_factory, password_hasher, database):
        """Initializer."""
        self.profile_model_factory = profile_model_factory
        self.password_hasher = password_hasher
        self.database = database


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()


class PasswordHasher:
    """Password hasher."""
