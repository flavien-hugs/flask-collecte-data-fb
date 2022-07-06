from flask import Flask

from apps.views import app
from apps.models import db

db.init_app(app)

@app.cli.command("init-db")
def create_db():
    db.init_db()
