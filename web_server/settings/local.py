from .base import BaseSettings


class LocalSettings(BaseSettings):
    ENV_NAME = 'LOCAL'
    SECRET_KEY = 'minitubel^&0b@k6u&n%ysfvys!1d3mh&(apmw$@f=&a^+e$0!)jzyn-j)'
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'minitube1',
            'USER': 'minitube1',
            'PASSWORD': 'minitube1',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

    CONFIGS = {
        'ELASTIC_SEARCH': {
            'BASE_URL': 'http://localhost:9200',
            'INDEXES': {
                'YOUTUBE_VIDEO': 'youtube_videos'
            }
        },
        'KAFKA': {
            'BROKERS': {
                'SEARCH_INDEX': ['localhost:9093'],
                'CRAWLER_INIT': ['localhost:9093'],
            },
            'TOPICS': {
                'SEARCH_INDEX': 'minitube-index',
                'CRAWLER_INIT': 'minitube-crawler-init',
            },
            'CONSUMERS': {
                'SEARCH_INDEX': 'minitube_index_grp1',
                'CRAWLER_INIT': 'minitube_crawler_init_grp1',
            }
        }
    }


LocalSettings.load_settings(__name__)
