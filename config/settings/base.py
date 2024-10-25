import os

from config import env, BASE_DIR

# BASE_DIR:
# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = BASE_DIR / "config"
APPS_DIR = BASE_DIR / "backend"


# DEBUG:
# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/fr/5.1/ref/settings/#debug
DEBUG = env("DEBUG")

# ALLOWED_HOSTS:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Wagtail applications
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail",
    "modelcluster",
    "taggit",
    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    # External applications
    "django_browser_reload",
    # Personal applications
    "app.blog",
    "app.home",
    "app.users",
    "app.utils",
    "app.base",
]

# GESTION DU MUTLI-SITES:
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# MIDDLEWARE:
# https://docs.djangoproject.com/fr/5.1/ref/settings/#middleware
# https://docs.djangoproject.com/fr/5.1/topics/http/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# URLS:
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        # https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/fr/5.1/ref/settings/#dirs
        "DIRS": [BASE_DIR / "templates"],
        # https://docs.djangoproject.com/fr/5.1/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/fr/5.1/ref/templates/api/#built-in-template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

# https://docs.djangoproject.com/fr/5.1/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# https://docs.djangoproject.com/fr/5.1/ref/settings/#databases
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

# https://docs.djangoproject.com/fr/5.1/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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

# MOTS DE PASSE:
# Configuration du chiffrement des mots de passe
# https://docs.djangoproject.com/fr/5.1/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/fr/5.1/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# INTERNATIONALISATION:
# https://docs.djangoproject.com/fr/5.1/topics/i18n/
# http://www.i18nguy.com/unicode/language-identifiers.html
# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-LANGUAGE_CODE
LANGUAGE_CODE = "fr-fr"

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = "Europe/Paris"

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
USE_L10N = True

# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-USE_TZ
USE_TZ = True

# AUTHENTIFICATION:
# https://docs.djangoproject.com/fr/5.1/topics/auth/customizing/#other-authentication-sources
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# https://docs.djangoproject.com/fr/5.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "users.User"

# https://docs.djangoproject.com/fr/5.1/ref/settings/#login-url
LOGIN_URL = "login"

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# https://docs.djangoproject.com/fr/5.1/ref/settings/#storages
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# https://docs.djangoproject.com/fr/5.1/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Fichiers statiques (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Méthode de stockage des fichiers statiques (production)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Fichiers media
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "home:home_page"
LOGOUT_REDIRECT_URL = "home:home_page"

# EMAIL
# https://docs.djangoproject.com/fr/5.1/ref/settings/
EMAIL_CONFIG = env.email(
    "DJANGO_EMAIL_URL",
    default="consolemail://",
)
globals().update(**EMAIL_CONFIG)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# EMAILS D'ADMIN
# https://docs.djangoproject.com/fr/5.1/ref/settings/#admins
ADMINS = [("""Laurent Jouron""", "jouronlaurent@hotmail.com")]

# https://docs.djangoproject.com/fr/5.1/ref/settings/#managers
MANAGERS = ADMINS

WAGTAIL_SITE_NAME = "Blog"

# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
WAGTAILADMIN_BASE_URL = "http://127.0.0.1:8000"

# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
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

# SECURITE
# https://docs.djangoproject.com/fr/5.1/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/fr/5.1/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False

# https://docs.djangoproject.com/fr/5.1/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=not DEBUG)
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
