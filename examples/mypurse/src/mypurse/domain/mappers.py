"""Domain model mappers."""


class ProfileMapper:
    """Profile domain model mapper."""

    def __init__(self, profile_model_factory, database):
        """Initializer."""
        self._profile_model_factory = profile_model_factory
        self._database = database

    def insert(self, profile):
        """Insert information into database."""
        profile.profile_id = 2345
        print('Insert profile - {0}'.format(profile))

    def update(self, profile):
        """Update information into database."""
        print('Update profile - {0}'.format(profile))
