"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, Length, AnyOf


class PetForm(FlaskForm):
    """Create a new Pet form """

    name = StringField(
        "Pet name",
        validators=[InputRequired()])

    # select field
    species = StringField(
        "Species",
        validators=[InputRequired(),
                    AnyOf(values=['cat', 'dog', 'porcupine'])])

    photo = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    age = SelectField(
        'Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')],
        validators=[InputRequired(),
                    AnyOf(values=['baby', 'young', 'adult', 'senior'])]
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
            Length(min=-1, max=500, message='No notes')]  # allow for text up to 500 chars
    )


class EditPetForm(FlaskForm):
    """Edit pet information"""

    photo = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
            Length(min=-1, max=500, message='No notes')]
    )
    available = BooleanField('Available for adoption')
