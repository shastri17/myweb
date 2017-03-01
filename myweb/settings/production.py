import os
from myweb.settings.base import *

ALLOWED_HOSTS=['52.43.69.172','localhost']

STATIC_ROOT=os.environ.get('STATIC_ROOT',None)

