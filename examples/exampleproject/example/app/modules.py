"""Functional modules container."""

import microjet.containers as containers
import microjet.providers as providers

import example.modules.users
import example.modules.photos

from .services import Services


class Photos(containers.Container):
    """Photos functional module."""

    models_factory = providers.Factory(example.modules.photos.Photo)

    manager = providers.Singleton(example.modules.photos.PhotosManager,
                                  photos_factory=models_factory.delegate(),
                                  db=Services.db)


class Users(containers.Container):
    """Users functional module."""

    models_factory = providers.Factory(example.modules.users.User)

    manager = providers.Singleton(example.modules.users.UsersManager,
                                  users_factory=models_factory.delegate(),
                                  photos_manager=Photos.manager,
                                  db=Services.db)
