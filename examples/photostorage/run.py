"""Application run script."""

import logging

from photostorage.app import PhotoStorage


if __name__ == '__main__':
    print(PhotoStorage.profiles_manager())
    print(PhotoStorage.profile_models_factory(profile_id=3598))

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
