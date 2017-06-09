"""Application run script."""

import datetime
import logging

from photostorage.app import PhotoStorage


if __name__ == '__main__':
    profile = PhotoStorage.profile_registration_service().register(
        password='secret', first_name='Roman', last_name='Mogylatov',
        birth_date=datetime.date(year=1988, month=5, day=4))

    password_verified = PhotoStorage.profile_password_service()\
        .verify_password(profile, 'secret')

    print(profile)
    print('Full name', profile.full_name)
    print('Age', profile.age)
    print('Password verified', password_verified)

    print(PhotoStorage.auth_service())
    print(PhotoStorage.auth_token_model_factory(auth_token_id=2359))

    print(PhotoStorage.photo_uploading_service())
    print(PhotoStorage.photo_model_factory(photo_id=1263))

    PhotoStorage.config.update({
        'host': '127.0.0.1',
        'port': 9090,
        'debug': True,
    })
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG)

    web_app = PhotoStorage.web_app_factory()
    web_app.router.add_get('/', PhotoStorage.web_handle)

    PhotoStorage.run_web_app(web_app)
