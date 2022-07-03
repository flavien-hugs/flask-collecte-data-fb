from flask import Flask

from .views import app
from .models import db

db.init_app(app)
