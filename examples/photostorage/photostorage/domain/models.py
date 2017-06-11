"""Domain models."""

import datetime
import string
import random

from microjet import models


class Profile(models.DomainModel):
    """Profile domain model."""

    profile_id = models.IntField()
    password_hash = models.StringField()
    first_name = models.StringField()
    last_name = models.StringField()
    birth_date = models.DateField()

    @property
    def full_name(self):
        """Return full name."""
        return ' '.join((self.first_name, self.last_name))

    @property
    def age(self):
        """Return age."""
        today = datetime.date.today()
        this_year_birthday = datetime.date(today.year,
                                           self.birth_date.month,
                                           self.birth_date.day)
        years_old = today.year - self.birth_date.year
        if today < this_year_birthday:
            years_old -= 1
        return years_old

    def set_password(self, password, hasher):
        """Set profile password."""
        self.password_hash = hasher.hash(password)

    def verify_password(self, password, hasher):
        """Verify that provided password matches profle password."""
        return hasher.verify(password, self.password_hash)


class AuthToken(models.DomainModel):
    """Authentication token domain model."""

    token_id = models.IntField()
    created_at = models.DateTimeField()
    expired_at = models.DateTimeField()
    status = models.StringField()
    profile = models.ModelField(Profile)

    def is_valid(self):
        """Check if token is actual."""
        if self.status == 'CANCELED':
            return False

        now = datetime.datetime.now()
        if self.expired_at > now:
            return False

        return True


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(Profile)


class AuthPasswordGenerator:
    """Generator of authentication passwords."""

    def __init__(self, password_length):
        """Initializer."""
        self._password_length = password_length
        self._characters = (string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + string.punctuation)

    def generate(self):
        """Generate new password."""
        return ''.join(random.choice(self._characters)
                       for _ in range(self._password_length))
