"""Domain model mappers."""


class ProfileMapper:
    """Profile domain model mapper."""

    def __init__(self, profile_model_factory, database):
        """Initializer."""
        self._profile_model_factory = profile_model_factory
        self._database = database

    def insert(self, profile):
        """Insert information into database."""
        # Insert data into database
        profile.profile_id = 2345
        print('Save profile - {0}'.format(profile))
