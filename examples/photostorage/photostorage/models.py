"""Domain models."""

from microjet import models


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()
    password_hash = models.StringField()


class ProfilePasswordHasher:
    """Profile password hasher."""

    def hash_password(self, password):
        """Hash password."""
        return '_'.join((password, 'hash'))


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(Profile)


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(Profile)
