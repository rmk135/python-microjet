"""Auth services."""


class AuthenticationService:
    """Authentication service."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self.auth_token_model_factory = auth_token_model_factory
        self.database = database
