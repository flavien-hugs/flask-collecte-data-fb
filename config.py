# To generate a new secret key:
# import random, string
# "".join([random.choice(string.printable) for _ in range(24)])

import os

SECRET_KEY = os.environ.get('SECRET_KEY')
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')

SQLALCHEMY_TRACK_MODIFICATIONS = False

if os.environ.get('DATABASE_URL') is None:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
