import os
from myweb.settings.base import *

ALLOWED_HOSTS=[u'52.43.69.172']

STATIC_ROOT=os.environ.get('STATIC_ROOT',None)

