"""Photo services."""


class PhotoUploadingService:
    """Photo uploading service."""

    def __init__(self, photo_model_factory, database):
        """Initializer."""
        self.photo_model_factory = photo_model_factory
        self.database = database
