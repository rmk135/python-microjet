"""Domain models."""

import datetime
import random

from microjet import models

from .utils import calculate_age


class ProfileInfo(models.DomainModel):
    """Profile information."""

    first_name = models.StringField()
    last_name = models.StringField()
    birth_date = models.DateField()
    updated_at = models.DateTimeField()

    @property
    def full_name(self):
        """Return full name."""
        return ' '.join((self.first_name, self.last_name))

    @property
    def age(self):
        """Return age."""
        return calculate_age(self.birth_date)

    def update(self, **attributes):
        """Update model attributes."""
        if 'first_name' in attributes:
            self.first_name = attributes['first_name']
        if 'last_name' in attributes:
            self.last_name = attributes['last_name']
        if 'birth_date' in attributes:
            self.birth_date = attributes['birth_date']

        if attributes:
            self.updated_at = datetime.datetime.now()


class ProfileInfoValidator:
    """Validator of profile information."""

    def __init__(self, minimal_age_limit):
        """Initializer."""
        self._minimal_age_limit = minimal_age_limit

    def validate_all(self, **attributes):
        """Validate all profile attributes."""
        return self._validate(attributes, __only_provided__=False)

    def validate_provided(self, **attributes):
        """Validate only provided profile attributes."""
        return self._validate(attributes, __only_provided__=True)

    def _validate(self, attributes, __only_provided__):
        errors = []

        if 'first_name' in attributes or __only_provided__ is False:
            errors.extend(
                self._validate_first_name(
                    attributes.get('first_name')))
        if 'last_name' in attributes or __only_provided__ is False:
            errors.extend(
                self._validate_last_name(
                    attributes.get('last_name')))
        if 'birth_date' in attributes or __only_provided__ is False:
            errors.extend(
                self._validate_birth_date(
                    attributes.get('birth_date')))

        if errors:
            error_message = ('Profile did not pass validation, '
                             'validation errors - [{0}]'.format(
                                 '; '.join(errors)))
            exception = RuntimeError(error_message)
            exception.errors = errors
            raise exception

        return attributes

    def _validate_first_name(self, first_name):
        if not first_name:
            return ['First name is required']
        return []

    def _validate_last_name(self, last_name):
        if not last_name:
            return ['Last name is required']
        return []

    def _validate_birth_date(self, birth_date):
        if not birth_date:
            return ['Birth date is required']
        return []

        age = calculate_age(birth_date)
        if age < self._minimal_age_limit:
            return ['Minimal age is - {0}, current is - {1}'.format(
                self._minimal_age_limit, age)]
        return []


class ProfileActivation(models.DomainModel):
    """Profile activation."""

    is_activated = models.BoolField()
    code = models.StringField()
    code_expired_at = models.DateTimeField()
    activated_at = models.DateTimeField()
    deactivated_at = models.DateTimeField()
    deactivated_reason = models.StringField()

    def initialize_activation_process(self, code, code_ttl):
        """Initialize activation process."""
        self.code = code
        self.code_expired_at = \
            datetime.datetime.now() + datetime.timedelta(seconds=code_ttl)

    def activate(self, code):
        """Activate profile."""
        if self.code != code:
            raise RuntimeError('Activation codes mismatch')
        self.is_activated = True
        self.activated_at = datetime.datetime.now()

    def deactivate(self, reason=None):
        """Deactivate profile."""
        self.is_activated = False
        self.deactivated_at = datetime.datetime.now()
        self.deactivation_reason = reason


class ProfileActivationCodeGenerator:
    """Generator of profile activation code."""

    def __init__(self, code_length, code_characters, code_ttl):
        """Initializer."""
        self._code_length = code_length
        self._code_characters = code_characters
        self._code_ttl = code_ttl

    def generate_activation_code(self):
        """Generate activation code."""
        code = ''.join(random.choice(self._code_characters)
                       for _ in range(self._code_length))
        return code, self._code_ttl


class ProfilePassword(models.DomainModel):
    """Profile password."""

    password_hash = models.StringField()

    def update(self, password_hash):
        """Update password."""
        self.password_hash = password_hash

    def verify(self, password_hash):
        """Verify if provided password matches current one."""
        return self.password_hash == password_hash


class ProfilePasswordValidator:
    """Validator of profile password."""

    def __init__(self, minimal_length):
        """Initializer."""
        self._minimal_length = minimal_length

    def validate(self, password):
        """Validate password."""
        if len(password) < self._minimal_length:
            raise RuntimeError('Password minimal length is {0}'.format(
                self._minimal_length))
        return password


class ProfilePasswordHasher:
    """Hasher of profile password."""

    def __init__(self, hasher, thread_pool, loop):
        """Initializer."""
        self._hasher = hasher
        self._thread_pool = thread_pool
        self._loop = loop

    async def hash(self, password):
        """Hash password."""
        return await self._loop.run_in_executor(self._thread_pool,
                                                self._hasher.hash,
                                                password)


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()
    info = models.ModelField(ProfileInfo)
    activation = models.ModelField(ProfileActivation)
    password = models.ModelField(ProfilePassword)
