"""Auth bundle."""

from microjet import models


class AuthManager:
    """Auth manager."""

    def __init__(self, auth_tokens_factory, database):
        """Initializer."""
        self.auth_tokens_factory = auth_tokens_factory
        self.database = database


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(object)  # profile domain model
