class UsersManager:

    def __init__(self, users_factory, photos_manager, db):
        self.users_factory = users_factory
        self.photos_manager = photos_manager
        self.db = db

    def get_users(self):
        return [self.users_factory(self.photos_manager.get_photos()),
                self.users_factory(self.photos_manager.get_photos())]
