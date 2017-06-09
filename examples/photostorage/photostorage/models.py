"""Domain models."""

import datetime

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


class AuthToken(models.DomainModel):
    """Auth token domain model."""

    token_id = models.IntField()
    profile = models.ModelField(Profile)


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(Profile)
