import os
SECRET_KEY = os.environ.get('SECRET_KEY_TEST')

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'test_app.db')

# ACTIVATE DEBUG

DEBUG = True
TESTING = True
LIVESERVER_PORT = 5000
LIVESERVER_TIMEOUT = 10
SERVER_NAME = "localhost:5000"

# FACEBOOK TEST USER DATA

FB_USER_NAME = "Ellen"
FB_USER_PW = "YOLOYOLO"
FB_USER_GENDER = 'female'
FB_USER_ID = 100018814390853
FB_USER_EMAIL = "ellen_rmilrcp_page@tfbnw.net"
