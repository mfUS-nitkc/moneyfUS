from .base import *  # noqa: F403

ALLOWED_HOSTS: list[str] = os.getenv("ALLOWED_HOSTS", "127.0.0.1, localhost").split(",")  # noqa: F405

DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"  # noqa: F405
