"""Domain services."""


class Registration:
    """Registration service.

    Responsibility of registration service is to register new profiles.
    """

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


class PasswordUpdate:
    """Password update service.

    Responsibility of password update service is to manipulate with updates of
    profile passwords.
    """

    def __init__(self, profile_password_hasher, profile_password_generator,
                 profile_mapper):
        """Initializer."""
        self._profile_password_hasher = profile_password_hasher
        self._profile_password_generator = profile_password_generator
        self._profile_mapper = profile_mapper

    def update_password(self, profile, current_password, new_password):
        """Update profile password."""
        current_password_verified = profile.verify_password(
            current_password, hashed_by=self._profile_password_hasher)

        if current_password_verified is False:
            raise RuntimeError('Profile password could not be updated without '
                               'passing verification of current password')

        profile.set_password(
            new_password, hashed_by=self._profile_password_hasher)

    def restore_password(self, profile):
        """Restore profile password by email."""
        new_password = \
            self._profile_password_generator.generate_random_password()

        profile.set_password(
            new_password, hashed_by=self._profile_password_hasher)

        return new_password


class Authentication:
    """Authentication service.

    Responsibility of authentication service is to authenticate profiles using
    various set of credentials (for example, email and password).
    """

    def __init__(self, profile_password_hasher, profile_mapper):
        """Initializer."""
        self._profile_password_hasher = profile_password_hasher
        self._profile_mapper = profile_mapper

    def authenticate(self, profile, password):
        """Try to authenticate profile by password."""
        return profile.verify_password(
            password, hashed_by=self._profile_password_hasher)

    def authenticate_by_email(self, email, password):
        """Try to authenticate profile by email and password."""
        profile = self._profile_mapper.find_by_email(email)
        return self.authenticate(profile, password)
