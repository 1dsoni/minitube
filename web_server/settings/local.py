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
            'PORT': '3308',
        }
    }

    CONFIGS = {
        'ELASTIC_SEARCH': {
            'BASE_URL': 'localhost:9200',
            'INDEXES': {
                'YOUTUBE_VIDEO': 'youtube_videos'
            }
        },
        'KAKFA': {
            'BROKERS': {
                'SEARCH_INDEX': ['kafka:9092']
            },
            'TOPICS': {
                'SEARCH_INDEX': 'minitube-index'
            },
            'CONSUMERS': {
                'SEARCH_INDEX': 'minitube_index_grp1'
            }
        }
    }


LocalSettings.load_settings(__name__)
