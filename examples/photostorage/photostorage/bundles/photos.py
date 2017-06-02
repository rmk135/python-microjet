"""Photos bundle."""

from microjet import models


class PhotoService:
    """Photo service."""

    def __init__(self, photo_model_factory, database):
        """Initializer."""
        self.photo_model_factory = photo_model_factory
        self.database = database


class Photo(models.DomainModel):
    """Photo domain model."""

    photo_id = models.IntField()
    profile = models.ModelField(object)  # profile domain model
