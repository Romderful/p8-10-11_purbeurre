"""Travis config."""


from . import *  # noqa: F403 F401


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
