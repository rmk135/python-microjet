"""Model providers container."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.models.users
import example.models.photos
import example.handlers.example

from .services import Services


class Models(containers.DeclarativeContainer):
    """Model providers container."""

    # Photos
    photos_factory = providers.Factory(example.models.photos.Photo)

    photos_manager = providers.Singleton(
        example.models.photos.PhotosManager,
        photos_factory=photos_factory.delegate(),
        db=Services.db)

    # Users
    users_factory = providers.Factory(example.models.users.User)

    users_manager = providers.Singleton(
        example.models.users.UsersManager,
        users_factory=users_factory.delegate(),
        photos_manager=photos_manager,
        db=Services.db)
