class PhotosManager:

    def __init__(self, photos_factory, db):
        self.photos_factory = photos_factory
        self.db = db

    def get_photos(self):
        return [self.photos_factory(), self.photos_factory()]


class Photo:
    pass
