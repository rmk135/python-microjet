"""Auth bundle."""

from microjet import models


class AuthManager:
    """Auth manager."""

    def __init__(self, auth_token_models_factory, database):
        """Initializer."""
        self.auth_token_models_factory = auth_token_models_factory
        self.database = database


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(object)  # profile domain model
