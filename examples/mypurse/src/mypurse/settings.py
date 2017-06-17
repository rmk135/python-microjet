"""Domain settings."""

import string


# Profile
MINIMAL_AGE_LIMIT = 14

# Profile activation
ACTIVATION_CODE_LENGTH = 32
ACTIVATION_CODE_CHARACTERS = (string.ascii_lowercase + string.ascii_uppercase +
                              string.digits)
ACTIVATION_CODE_TTL = 3600

# Profile password
MINIMAL_PASSWORD_LENGTH = 8
