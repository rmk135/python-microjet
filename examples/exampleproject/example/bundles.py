"""Functional bundles container."""

from microjet import containers
from microjet import providers

from .app.bundles import profiles
from .app.bundles import auth
from .app.bundles import photos

from .services import Services


class Profiles(containers.Container):
    """Profiles bundle container."""

    profiles_factory = providers.Factory(profiles.Profile)

    password_hasher_factory = providers.Factory(profiles.PasswordHasher)

    manager = providers.Singleton(profiles.ProfilesManager,
                                  profiles_factory=profiles_factory.delegate(),
                                  password_hasher=password_hasher_factory,
                                  database=Services.db)


class Auth(containers.Container):
    """Auth bundle container."""

    auth_tokens_factory = providers.Factory(auth.AuthToken)

    manager = providers.Singleton(
        auth.AuthManager,
        auth_tokens_factory=auth_tokens_factory.delegate(),
        database=Services.db)


class Photos(containers.Container):
    """Photos bundle container."""

    photos_factory = providers.Factory(photos.Photo)

    manager = providers.Singleton(photos.PhotosManager,
                                  photos_factory=photos_factory.delegate(),
                                  database=Services.db)
