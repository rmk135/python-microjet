"""Model providers container."""

import microjet.core.models as models

import example.models.users
import example.models.photos
import example.handlers.example

from .services import Services


class PhotoModels(models.Container):
    """Photo model providers container."""

    model_factory = models.DelegatedFactory(example.models.photos.Photo)

    manager = models.Singleton(example.models.photos.PhotosManager,
                               photos_factory=model_factory,
                               db=Services.db)


class UserModels(models.Container):
    """User model providers container."""

    model_factory = models.DelegatedFactory(example.models.users.User)

    manager = models.Singleton(example.models.users.UsersManager,
                               users_factory=model_factory,
                               photos_manager=PhotoModels.manager,
                               db=Services.db)
