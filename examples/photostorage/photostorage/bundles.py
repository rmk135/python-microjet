"""Functional bundles container."""

from microjet.containers import Container
from microjet.providers import Factory, Singleton

from .app.bundles import profiles
from .app.bundles import auth
from .app.bundles import photos

from .services import Services


class Profiles(Container):
    """Profiles bundle container."""

    profiles_factory = Factory(profiles.Profile)

    password_hasher_factory = Factory(profiles.PasswordHasher)

    profiles_manager = Singleton(profiles.ProfilesManager,
                                 profiles_factory=profiles_factory.delegate(),
                                 password_hasher=password_hasher_factory,
                                 database=Services.database)


class Auth(Container):
    """Auth bundle container."""

    auth_tokens_factory = Factory(auth.AuthToken)

    auth_manager = Singleton(
        auth.AuthManager,
        auth_tokens_factory=auth_tokens_factory.delegate(),
        database=Services.database)


class Photos(Container):
    """Photos bundle container."""

    photos_factory = Factory(photos.Photo)

    photos_manager = Singleton(photos.PhotosManager,
                               photos_factory=photos_factory.delegate(),
                               database=Services.database)
