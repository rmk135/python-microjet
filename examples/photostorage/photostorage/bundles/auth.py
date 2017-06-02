"""Auth bundle."""

from microjet import models


class AuthService:
    """Auth service."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self.auth_token_model_factory = auth_token_model_factory
        self.database = database


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(object)  # profile domain model
