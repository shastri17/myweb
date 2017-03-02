import os
from myweb.settings.base import *
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['52.43.69.172','localhost']
STATIC_ROOT = os.environ.get('STATIC_ROOT', None)

