import os
from flask import Flask

from .views import app
from . import models

models.db.init_app(app)

@app.cli.command("init-db")
def create_db():
    models.init_db()
