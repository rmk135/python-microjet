"""Domain services."""


class ProfileRegistrationService:
    """Profile registration service."""

    def __init__(self, profile_model_factory, profile_password_hasher,
                 profile_mapper):
        """Initializer."""
        self._profile_model_factory = profile_model_factory
        self._profile_password_hasher = profile_password_hasher
        self._profile_mapper = profile_mapper

    def register(self, **profile_data):
        """Register profile."""
        try:
            raw_password = profile_data.pop('password')
        except KeyError:
            raise RuntimeError('Profile password is required')

        profile = self._profile_model_factory(**profile_data)
        profile.set_password(
            raw_password, hashed_by=self._profile_password_hasher)

        self._profile_mapper.insert(profile)

        return profile


class AuthenticationService:
    """Authentication service."""

    def __init__(self, auth_token_model_factory, database):
        """Initializer."""
        self._auth_token_model_factory = auth_token_model_factory
        self._database = database

    def sign_in(self, profile, password):
        """Sign profile in."""
        password_verified = self._password_hasher.verify(password,
                                                         profile.password)
        if password_verified is False:
            return False

        auth_token = self._auth_token_model_factory(profile=profile)
        self._auth_token_mapper.insert(auth_token)

        return auth_token

    def sign_out(self, auth_token):
        """Sign out particular session by auth token."""
