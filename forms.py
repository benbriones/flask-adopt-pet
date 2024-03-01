"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL, Length


class PetForm(FlaskForm):
    """  """

    name = StringField(
        "Pet name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired()])

# TODO: Make url optional
    photo = StringField(
        "Photo URL",
        validators=[InputRequired(), URL()])

    age = SelectField(
        'Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')],
        validators=[InputRequired()]
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
            Length(min=-1, max=500, message='No notes')]
    )
