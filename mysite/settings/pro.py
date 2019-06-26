from .base import *
import platform
DEBUG = False
ADMINS = (
('Warren Cheng', 'warren.y.cheng@gmail.com'),
)
ALLOWED_HOSTS = ['*']

if platform.release() == "4.18.0-20-generic":
    STATIC_ROOT = "/home/jn8029/Desktop/django2/mysite/mysite/static/"