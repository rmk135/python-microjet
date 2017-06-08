"""Domain model mappers."""


class ProfileMapper:
    """Profile domain model mapper."""

    def __init__(self, profile_model_factory, database):
        """Initializer."""
        self.profile_model_factory = profile_model_factory
        self.database = database

    def insert(self, profile):
        """Insert information into database."""
        # Insert data into database
        profile.profile_id = 2345


class AuthTokenMapper:
    """Auth token domain model mapper."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self.auth_token_model_factory = auth_token_model_factory
        self.database = database


class PhotoMapper:
    """Photo domain model mapper."""

    def __init__(self, photo_model_factory, database):
        """Initializer."""
        self.photo_model_factory = photo_model_factory
        self.database = database
