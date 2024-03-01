from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Makes a Pet"""

    __tablename__ = 'pets'

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    name = db.Column(
        db.Text,
        nullable = False
    )

    species = db.Column(
        db.Text,
        nullable = False
    )

    photo_url = db.Column(
        db.Text,
        nullable = True,
        default = ''
    )

    age = db.Column(
        db.Text,
        nullable = False
    )

    notes = db.Column(
        db.Text,
        nullable = True
    )

    available = db.Column(
        db.Boolean,
        nullable = False,
        default = True
    )


