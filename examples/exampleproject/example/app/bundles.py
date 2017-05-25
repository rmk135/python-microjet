"""Functional bundles container."""

import microjet.containers as containers
import microjet.providers as providers

import example.bundles.users
import example.bundles.photos

from .services import Services


class Photos(containers.Container):
    """Photos functional bundle."""

    models_factory = providers.Factory(example.bundles.photos.Photo)

    manager = providers.Singleton(example.bundles.photos.PhotosManager,
                                  photos_factory=models_factory.delegate(),
                                  db=Services.db)


class Users(containers.Container):
    """Users functional bundle."""

    models_factory = providers.Factory(example.bundles.users.User)

    manager = providers.Singleton(example.bundles.users.UsersManager,
                                  users_factory=models_factory.delegate(),
                                  photos_manager=Photos.manager,
                                  db=Services.db)
