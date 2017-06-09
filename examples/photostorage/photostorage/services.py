"""Services."""


class ProfilePasswordService:
    """Profile password hasher based on scrypt algorithm."""

    def __init__(self, profile_password_hasher):
        """Initializer."""
        self._profile_password_hasher = profile_password_hasher

    def set_password(self, profile, password):
        """Set profile password."""
        profile.password_hash = self._profile_password_hasher.hash(password)
        return profile

    def verify_password(self, profile, provided_password):
        """Verify that provided password matches to profile actual password."""
        return self._profile_password_hasher.verify(provided_password,
                                                    profile.password_hash)


class ProfileRegistrationService:
    """Profile registration service."""

    def __init__(self, profile_model_factory, profile_password_service,
                 profile_mapper):
        """Initializer."""
        self._profile_model_factory = profile_model_factory
        self._profile_password_service = profile_password_service
        self._profile_mapper = profile_mapper

    def register(self, **profile_data):
        """Register profile."""
        try:
            password = profile_data.pop('password')
        except KeyError:
            raise RuntimeError('Profile password is required')

        profile = self._profile_model_factory(**profile_data)

        self._profile_password_service.set_password(profile, password)
        self._profile_mapper.insert(profile)

        return profile


class AuthenticationService:
    """Authentication service."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self._auth_token_model_factory = auth_token_model_factory
        self._database = database


class PhotoUploadingService:
    """Photo uploading service."""

    def __init__(self, photo_model_factory, database):
        """Initializer."""
        self._photo_model_factory = photo_model_factory
        self._database = database
