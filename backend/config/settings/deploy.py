from .base import *  # noqa: F403

DEBUG = False
ALLOWED_HOSTS: list[str] = os.getenv("ALLOWED_HOSTS").split(",")  # noqa: F405
