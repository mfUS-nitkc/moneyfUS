from .base import *  # noqa: F403

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ["127.0.0.1", "localhost"])  # noqa: F405
