from .base import *

DEBUG = False
ALLOWED_HOSTS: list[str] = os.getenv('ALLOWED_HOSTS').split(',')
