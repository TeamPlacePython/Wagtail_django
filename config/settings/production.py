from .base import *  # noqa: F403
from .base import env

# GENERAL
# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-SECRET_KEY
SECRET_KEY = env("SECRET_KEY")

# DEBUG:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-SECRET_KEY
DEBUG = env.bool("DEBUG", False)

# ALLOWED HOSTS
# https://docs.djangoproject.com/fr/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["laurentjouron.com"])

# BASE DE DONNEES:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

# SECURITE
# https://docs.djangoproject.com/fr/5.1/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/fr/5.1/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)

# https://docs.djangoproject.com/fr/5.1/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/fr/5.1/ref/settings/#session-cookie-name
SESSION_COOKIE_NAME = "__Secure-sessionid"

# https://docs.djangoproject.com/fr/5.1/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/fr/5.1/ref/settings/#csrf-cookie-name
CSRF_COOKIE_NAME = "__Secure-csrftoken"

# https://docs.djangoproject.com/fr/5.1/topics/security/#ssl-https
# https://docs.djangoproject.com/fr/5.1/ref/settings/#secure-hsts-seconds
# TODO: Réglez d'abord cette valeur à 60 secondes, puis à 518400 une fois que
# vous aurez prouvé que la première fonctionne.
SECURE_HSTS_SECONDS = 60

# https://docs.djangoproject.com/fr/5.1/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS",
    default=True,
)

# https://docs.djangoproject.com/fr/5.1/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=True)

# https://docs.djangoproject.com/fr/5.1/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "SECURE_CONTENT_TYPE_NOSNIFF",
    default=True,
)

# https://docs.djangoproject.com/fr/5.1/ref/settings/
EMAIL_CONFIG = env.email(
    "EMAIL_URL",
    default="consolemail://",
)
globals().update(**EMAIL_CONFIG)

# https://docs.djangoproject.com/fr/5.1/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL",
    default="<noreply@laurentjouron.com>",
)

# https://docs.djangoproject.com/fr/5.1/ref/settings/#server-email
SERVER_EMAIL = env("SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

# https://docs.djangoproject.com/fr/5.1/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="",
)

# ADMIN
ADMIN_URL = env("ADMIN_URL")

# Journalisation
# https://docs.djangoproject.com/fr/5.1/ref/settings/#logging
# Voir https://docs.djangoproject.com/fr/5.1/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

# Wagtail settings
WAGTAILADMIN_BASE_URL = "https://laurentjouron.com"
