"""Functional bundles container."""

from microjet import containers
from microjet import providers

from .app.bundles import photos
from .app.bundles import users

from .services import Services


class Photos(containers.Container):
    """Photos functional bundle."""

    models_factory = providers.Factory(photos.Photo)

    manager = providers.Singleton(photos.PhotosManager,
                                  photos_factory=models_factory.delegate(),
                                  db=Services.db)


class Users(containers.Container):
    """Users functional bundle."""

    models_factory = providers.Factory(users.User)

    manager = providers.Singleton(users.UsersManager,
                                  users_factory=models_factory.delegate(),
                                  photos_manager=Photos.manager,
                                  db=Services.db)
