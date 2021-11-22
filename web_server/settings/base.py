"""Class based settings for complex settings inheritance."""

import inspect
import sys
from pathlib import Path


class BaseSettings(object):
    @classmethod
    def load_settings(cls, module_name):
        """
        Export class variables and properties to module namespace.
        This will export and class variable that is all upper case and doesn't
        begin with ``_``. These members will be set as attributes on the module
        ``module_name``.
        """
        self = cls()
        module = sys.modules[module_name]
        for (member, value) in inspect.getmembers(self):
            if member.isupper() and not member.startswith('_'):
                if isinstance(value, property):
                    value = value.fget(self)
                setattr(module, member, value)

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    INSTALLED_APPS = [
        'minitube.apps.search.apps.SearchConfig',
        'minitube.apps.indexer.apps.IndexerConfig',
        'minitube.apps.crawler.apps.CrawlerConfig',
        'minitube.apps.client.apps.ClientConfig',
        'minitube.apps.tracer.apps.TracerConfig',
        'minitube.apps.api_key.apps.ApiKeyConfig'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'minitube.apps.client.middlewares.ClientAuthMiddleware',
        'minitube.apps.tracer.middlewares.TracerMiddleware'
    ]

    ROOT_URLCONF = 'minitube.urls'

    WSGI_APPLICATION = 'wsgi.application'

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 10
    }

    API_TIMEOUT = 5  # in seconds
