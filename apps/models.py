from flask_sqlalchemy import SQLAlchemy

from .views import app

db = SQLAlchemy(app)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer(), nullable=True)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, gender, description):
        self.gender = gender
        self.description = description


db.create_all()
