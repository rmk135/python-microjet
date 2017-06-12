"""Domain models."""

import datetime
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

    def set_password(self, password, *, hashed_by):
        """Set profile password."""
        self.password_hash = hashed_by.hash(password)

    def verify_password(self, password, *, hashed_by):
        """Verify that provided password matches profle password."""
        return hashed_by.verify(password, self.password_hash)


class RandomPasswordGenerator:
    """Generator of random passwords."""

    def __init__(self, password_length, characters):
        """Initializer."""
        self._password_length = password_length
        self._characters = characters

    def generate_random_password(self):
        """Generate random password."""
        return ''.join(random.choice(self._characters)
                       for _ in range(self._password_length))
