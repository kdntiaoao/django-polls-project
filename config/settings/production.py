import environ

from .base import *

env = environ.Env()
# Read .env if exists
environ.Env.read_env(str(BASE_DIR / ".env"))


#####################
# Security settings #
#####################

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


############
# Database #
############

DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "ATOMIC_ZONE": True,
        "TIME_ZONE": "Asia/Tokyo",
    }
}
