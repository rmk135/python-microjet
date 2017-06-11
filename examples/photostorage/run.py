"""Application run script."""

import datetime
import logging

from photostorage.app import PhotoStorage


if __name__ == '__main__':
    profile = PhotoStorage.profile_registration_service().register(
        password='secret', first_name='Roman', last_name='Mogylatov',
        birth_date=datetime.date(year=1988, month=5, day=4))

    password_verified = profile.verify_password(
        'secret', hasher=PhotoStorage.profile_password_hasher_factory())

    print(profile)
    print('Full name', profile.full_name)
    print('Age', profile.age)
    print('Password verified', password_verified)

    PhotoStorage.config.update({
        'host': '127.0.0.1',
        'port': 9090,
        'debug': True,
    })
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)
