from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from config import env

# DEBUG:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-SECRET_KEY
SECRET_KEY = env(
    "SECRET_KEY",
    default="3E9AEJf1l1JNJnTwPmwhkKCpGgD6RP8rNALkFyqnhLs",
)

# ALLOWED_HOSTS:
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"]
)

# EMAIL
# https://docs.djangoproject.com/fr/5.1/ref/settings/
EMAIL_BACKEND = env.email(
    "DJANGO_EMAIL_URL",
    default="consolemail://",
)

# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# INSTALLED_APPS += ["debug_toolbar"]

# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# WAGTAILADMIN_BASE_URL required for notification emails
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Désactive le panneau de profilage à cause d'un problème avec Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
