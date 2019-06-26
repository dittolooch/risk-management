from .base import *
from configparser import RawConfigParser
import os
config = RawConfigParser()
config.read('/opt/settings.ini')
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb_test',
        'USER':config.get('section','MYSQL_ACCOUNT'),
        'PASSWORD':config.get('section', 'MYSQL_PASSWORD'),
        'HOST':'3.105.226.33',
        'PORT':'3306'
    }
}


#mysql --defaults-extra-file=/opt/settings.ini djangodb_test < /opt/mysql_backup/djangodb-$(date -I).sql
