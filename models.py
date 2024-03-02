from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://t3.ftcdn.net/jpg/03/45/05/92/360_F_345059232_CPieT8RIWOUk4JqBkkWkIETYAkmz2b75.jpg'


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
        primary_key=True,
        autoincrement=True
    )


    name = db.Column(
        db.Text,
        nullable=False
    )

    species = db.Column(
        db.Text,
        nullable=False
    )

    photo = db.Column(
        db.Text,
        nullable=True,
        default=DEFAULT_IMAGE_URL
    )

    age = db.Column(
        db.Text,
        nullable=False
    )
    # default = '' nullable = false, better to deal with empty strings than null
    notes = db.Column(
        db.Text,
        nullable=True
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
