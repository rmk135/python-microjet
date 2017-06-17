"""Utilities module."""

import datetime


def calculate_age(birth_date):
    """Return age in years based on given birth date."""
    today = datetime.date.today()
    this_year_birthday = datetime.date(today.year,
                                       birth_date.month,
                                       birth_date.day)
    years_old = today.year - birth_date.year
    if today < this_year_birthday:
        years_old -= 1
    return years_old
