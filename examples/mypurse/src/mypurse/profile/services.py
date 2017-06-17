"""Domain services."""


class ProfileRegistration:
    """Registration service.

    Responsibility of profile registration service is to register new profiles.
    """

    def __init__(self, profile_model_factory, profile_mapper, info_validator,
                 activation_code_generator, password_validator,
                 password_hasher):
        """Initializer."""
        self._profile_model_factory = profile_model_factory
        self._profile_mapper = profile_mapper

        self._info_validator = info_validator

        self._password_validator = password_validator
        self._password_hasher = password_hasher

        self._activation_code_generator = activation_code_generator

    async def register(self, first_name, last_name, birth_date, password):
        """Register profile."""
        # Main model
        profile = self._profile_model_factory()

        profile.info.update(
            **self._info_validator.validate_all(first_name=first_name,
                                                last_name=last_name,
                                                birth_date=birth_date))
        profile.password.update(
            await self._password_hasher.hash(
                self._password_validator.validate(password)))

        # Activation
        activation_code, activation_code_ttl = \
            self._activation_code_generator.generate_activation_code()

        profile.activation.initialize_activation_process(
            code=activation_code, code_ttl=activation_code_ttl)

        # Mapping
        await self._profile_mapper.insert(profile)

        return profile


class ProfileUpdater:
    """Profile updater service.

    Responsibility of profile updater service is to manipulate with updates of
    profile data.
    """

    def __init__(self, info_validator, password_validator, password_hasher,
                 profile_mapper):
        """Initializer."""
        self._info_validator = info_validator
        self._password_validator = password_validator
        self._password_hasher = password_hasher
        self._profile_mapper = profile_mapper

    async def update_info(self, profile, **attributes):
        """Update profile info."""
        profile.info.update(
            **self._info_validator.validate_provided(**attributes))
        await self._profile_mapper.update(profile)

    async def update_password(self, profile, new_password, old_password):
        """Update profile password."""
        old_password_verified = profile.password.verify(
            await self._password_hasher.hash(old_password))

        if old_password_verified is False:
            raise RuntimeError('Old password does not match')

        profile.password.update(
            await self._password_hasher.hash(
                self._password_validator.validate(new_password)))

        await self._profile_mapper.update(profile)

#     def update_profile_data(self, profile, current_password, new_password):
#         """Update profile password."""
#         current_password_verified = profile.verify_password(
#             current_password, hashed_by=self._profile_password_hasher)
#
#         if current_password_verified is False:
#             raise RuntimeError('Profile password could not be updated without '
#                                'passing verification of current password')
#
#         profile.set_password(
#             new_password, hashed_by=self._profile_password_hasher)
#
#         self._profile_mapper.update(profile)
#
#     def restore_password(self, profile):
#         """Restore profile password by email."""
#         new_password = \
#             self._profile_password_generator.generate_random_password()
#
#         profile.set_password(
#             new_password, hashed_by=self._profile_password_hasher)
#
#         self._profile_mapper.update(profile)
#
#         return new_password


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


class RandomPasswordGenerator:
    """Generator of random passwords."""

    def __init__(self, password_length, characters):
        """Initializer."""
        self._password_length = password_length
        self._characters = characters

    def generate_random_password(self):
        """Generate random password."""
        import random  # noqa
        return ''.join(random.choice(self._characters)
                       for _ in range(self._password_length))
