"""Application run script."""

import logging

from photostorage.app import PhotoStorage


if __name__ == '__main__':
    print(PhotoStorage.profile_registration_service())
    print(PhotoStorage.profile_model_factory(profile_id=3598))

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
