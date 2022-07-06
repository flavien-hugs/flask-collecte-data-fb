import enum
import logging as lg
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 0
    female = 1
    other = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Enum(Gender), nullable=True)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, gender, description):
        self.gender = gender
        self.description = description


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content(Gender['female'], "Django framework !"))
    db.session.add(Content(Gender['male'], "Flask micro-framework !"))
    db.session.commit()
    lg.warning('Database initialized !')
