import os
from pathlib import Path

from config import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "config"
APPS_DIR = BASE_DIR / "backend"

SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-^&p@x!w%0!&%0!^&p@x!w%0!^&p@x!w%0!^&p@x!w%0!^&p@x!w%0!^&p@x!w%0!^&p@x!w%0!^&p@x!w%0!",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "taggit",
    "django_browser_reload",
    "modelcluster",
    "backend.blog",
    "backend.home",
    "backend.users",
    "backend.utils",
    "backend.base",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": env.db(
        default="sqlite:///db.sqlite3",
    )
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("POSTGRES_DB", "mydatabase"),
#         "USER": env("POSTGRES_USER", "myuser"),
#         "PASSWORD": env("POSTGRES_PASSWORD", "mypassword"),
#         "HOST": env("POSTGRES_HOST", "localhost"),
#         "PORT": env("POSTGRES_PORT", "5432"),
#         "CONN_MAX_AGE": env.int("CONN_MAX_AGE", default=600),
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("MYSQL_DB", "mydatabase"),
#         "USER": env("MYSQL_USER", "myuser"),
#         "PASSWORD": env("MYSQL_PASSWORD", "mypassword"),
#         "HOST": env("MYSQL_HOST", "localhost"),
#         "PORT": env("MYSQL_PORT", "5432"),
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.oracle",
#         "NAME": env("ORACLE_DB", "mydatabase"),
#         "USER": env("ORACLE_USER", "myuser"),
#         "PASSWORD": env("ORACLE_PASSWORD", "mypassword"),
#         "HOST": env("ORACLE_HOST", "localhost"),
#         "PORT": env("ORACLE_PORT", "5432"),
#     }
# }

# Gestion de la session et du cache
# SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 9},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Localisation
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache.
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Automatically compress static files
WHITENOISE_USE_FINDERS = True

# Fichiers statiques (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Méthode de stockage des fichiers statiques (production)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Fichiers media
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "home:home_page"
LOGOUT_REDIRECT_URL = "home:home_page"

# Configuration des emails
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_SUBJECT_PREFIX = "[]"
DEFAULT_FROM_EMAIL = ""
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-email-password")

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WAGTAIL_SITE_NAME = "Blog"
WAGTAILADMIN_BASE_URL = "http://127.0.0.1"

WAGTAILDOCS_EXTENSIONS = [
    "pdf",
    "doc",
    "docx",
    "txt",
    "ppt",
    "pptx",
    "xls",
    "xlsx",
    "csv",
    "mp3",
    "mp4",
    "mov",
    "avi",
    "mkv",
    "key",
    "odt",
    "rtf",
    "zip",
]
WAGTAILIMAGES_EXTENSIONS = [
    "gif",
    "jpg",
    "jpeg",
    "png",
    "svg",
    "mp4",
    "mov",
    "avi",
    "mkv",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

# Sécurisation supplémentaire
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=not DEBUG)
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
