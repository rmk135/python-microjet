"""Functional modules container."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.modules.users
import example.modules.photos

from .services import Services


class Photos(containers.DeclarativeContainer):
    """Photos functional module."""

    models_factory = providers.Factory(example.modules.photos.Photo)

    manager = providers.Singleton(example.modules.photos.PhotosManager,
                                  photos_factory=models_factory.delegate(),
                                  db=Services.db)


class Users(containers.DeclarativeContainer):
    """Users functional module."""

    models_factory = providers.Factory(example.modules.users.User)

    manager = providers.Singleton(example.modules.users.UsersManager,
                                  users_factory=models_factory.delegate(),
                                  photos_manager=Photos.manager,
                                  db=Services.db)
