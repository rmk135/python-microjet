"""Photos bundle."""

from microjet import models


class PhotosManager:
    """Photos manager."""

    def __init__(self, photo_models_factory, database):
        """Initializer."""
        self.photo_models_factory = photo_models_factory
        self.database = database


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(object)  # profile domain model
