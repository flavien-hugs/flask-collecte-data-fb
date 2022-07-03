# To generate a new secret key:
# import random, string
# "".join([random.choice(string.printable) for _ in range(24)])

import os

SECRET_KEY = os.environ.get('SECRET_KEY')
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
