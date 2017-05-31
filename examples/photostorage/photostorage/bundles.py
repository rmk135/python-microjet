"""Functional bundles container."""

from microjet.containers import Container
from microjet.providers import Factory, Singleton

from .app.bundles import profiles
from .app.bundles import auth
from .app.bundles import photos

from .services import Services


class Profiles(Container):
    """Profiles bundle container."""

    models_factory = Factory(profiles.Profile)

    password_hasher_factory = Factory(profiles.PasswordHasher)

    manager = Singleton(profiles.ProfilesManager,
                        profiles_factory=models_factory.delegate(),
                        password_hasher=password_hasher_factory,
                        database=Services.database)


class Auth(Container):
    """Auth bundle container."""

    models_factory = Factory(auth.AuthToken)

    manager = Singleton(auth.AuthManager,
                        auth_tokens_factory=models_factory.delegate(),
                        database=Services.database)


class Photos(Container):
    """Photos bundle container."""

    models_factory = Factory(photos.Photo)

    manager = Singleton(photos.PhotosManager,
                        photos_factory=models_factory.delegate(),
                        database=Services.database)
