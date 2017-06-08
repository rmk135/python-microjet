"""Services."""


class ProfileRegistrationService:
    """Profile registration service."""

    def __init__(self, profile_model_factory, profile_password_hasher,
                 profile_mapper):
        """Initializer."""
        self.profile_model_factory = profile_model_factory
        self.profile_password_hasher = profile_password_hasher
        self.profile_mapper = profile_mapper

    def register(self, **profile_data):
        """Register profile."""
        try:
            password = profile_data.pop('password')
        except KeyError:
            raise RuntimeError('Profile password is required')
        else:
            password_hash = self.profile_password_hasher.hash_password(
                password)

        profile = self.profile_model_factory(password_hash=password_hash,
                                             **profile_data)

        self.profile_mapper.insert(profile)

        return profile


class AuthenticationService:
    """Authentication service."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self.auth_token_model_factory = auth_token_model_factory
        self.database = database


class PhotoUploadingService:
    """Photo uploading service."""

    def __init__(self, photo_model_factory, database):
        """Initializer."""
        self.photo_model_factory = photo_model_factory
        self.database = database
