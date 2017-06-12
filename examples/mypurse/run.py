"""Application run script."""

import datetime
import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'src'))  # noqa

from mypurse.app import MyPurseApp


if __name__ == '__main__':
    MyPurseApp.config.update({
        'host': '127.0.0.1',
        'port': 9090,
        'debug': True,
    })
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)

    # Basic scenarios
    profile = MyPurseApp.registration_service().register(
        password='secret', first_name='Roman', last_name='Mogylatov',
        birth_date=datetime.date(year=1988, month=5, day=4))

    password_verified = MyPurseApp.authentication_service()\
        .authenticate(profile, password='secret')

    restored_password = MyPurseApp.password_update_service().\
        restore_password(profile)

    print(profile)
    print('Full name', profile.full_name)
    print('Age', profile.age)
    print('Password verified', password_verified)
    print('Password restored, new password', restored_password)
