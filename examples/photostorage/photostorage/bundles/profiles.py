"""Profiles bundle."""

from microjet import models


class ProfilesManager:
    """Profiles manager."""

    def __init__(self, profile_models_factory, password_hasher, database):
        """Initializer."""
        self.profile_models_factory = profile_models_factory
        self.password_hasher = password_hasher
        self.database = database


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()


class PasswordHasher:
    """Password hasher."""
