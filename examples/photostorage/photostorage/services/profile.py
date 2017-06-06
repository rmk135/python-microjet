"""Profile services."""


class ProfileRegistrationService:
    """Profile registration service."""

    def __init__(self, profile_model_factory, password_hasher, database):
        """Initializer."""
        self.profile_model_factory = profile_model_factory
        self.password_hasher = password_hasher
        self.database = database
