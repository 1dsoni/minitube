import os

from .base import BaseSettings


class ENV_VARS:
    DJANGO_SETTINGS_MODULE = os.environ['DJANGO_SETTINGS_MODULE']

    DJANGO_SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

    KAKFA_BROKERS = os.environ['KAKFA_BROKERS'].split(',')
    KAKFA_SEARCH_INDEX_TOPIC = os.environ['KAKFA_SEARCH_INDEX_TOPIC']
    KAKFA_SEARCH_INDEX_CONSUMER_GRP = os.environ[
        'KAKFA_SEARCH_INDEX_CONSUMER_GRP']

    ELASTIC_SEARCH_BASE_URL = os.environ['ELASTIC_SEARCH_BASE_URL']
    ES_INDEX_YT = os.environ['ES_INDEX_YT']

    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_NAME = os.environ['DB_NAME']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

class ProductionSettings(BaseSettings):
    ENV_NAME = 'PRODUCTION'

    SECRET_KEY = ENV_VARS.DJANGO_SECRET_KEY

    DEBUG = False

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': ENV_VARS.DB_NAME,
            'USER': ENV_VARS.DB_USER,
            'PASSWORD': ENV_VARS.DB_PASSWORD,
            'HOST': ENV_VARS.DB_HOST,
            'PORT': ENV_VARS.DB_PORT,
        }
    }

    CONFIGS = {
        'ELASTIC_SEARCH': {
            'BASE_URL': ENV_VARS.ELASTIC_SEARCH_BASE_URL,
            'INDEXES': {
                'YOUTUBE_VIDEO': ENV_VARS.ES_INDEX_YT
            }
        },
        'KAFKA': {
            'BROKERS': {
                'SEARCH_INDEX': ENV_VARS.KAKFA_BROKERS,
                'CRAWLER_INIT': ['kafka:9092'],
            },
            'TOPICS': {
                'SEARCH_INDEX': ENV_VARS.KAKFA_SEARCH_INDEX_TOPIC,
                'CRAWLER_INIT': 'minitube-crawler-init'
            },
            'CONSUMERS': {
                'SEARCH_INDEX': ENV_VARS.KAKFA_SEARCH_INDEX_CONSUMER_GRP,
                'CRAWLER_INIT': 'minitube_crawler_init_grp1'
            }
        }
    }


ProductionSettings.load_settings(__name__)
