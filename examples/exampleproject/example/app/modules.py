"""Functional modules."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.models.users
import example.models.photos

from .services import Services


class Photos(containers.DeclarativeContainer):
    """Photos functional module."""

    models_factory = providers.Factory(example.models.photos.Photo)

    manager = providers.Singleton(example.models.photos.PhotosManager,
                                  photos_factory=models_factory.delegate(),
                                  db=Services.db)


class Users(containers.DeclarativeContainer):
    """Users functional module."""

    models_factory = providers.Factory(example.models.users.User)

    manager = providers.Singleton(example.models.users.UsersManager,
                                  users_factory=models_factory.delegate(),
                                  photos_manager=Photos.manager,
                                  db=Services.db)
