import environ

from .base import *

env = environ.Env()
# Read .env if exists
environ.Env.read_env(str(BASE_DIR / ".env"))


#####################
# Security settings #
#####################

DEBUG = True

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["*"]


############
# Database #
############

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


########################
# Django Debug Toolbar #
########################

if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INTERNAL_IPS = ["127.0.0.1"]
