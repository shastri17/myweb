import os
from myweb.settings.base import *

ALLOWED_HOSTS=['172.31.31.158','localhost']

STATIC_ROOT=os.environ.get('STATIC_ROOT',None)

