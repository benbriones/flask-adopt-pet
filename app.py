import os
from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.conf['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.get('/')
def display_homepage():
    """displays the homepage, with all Pets"""
    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def disply_pets_form():
    """  """

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo=photo,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template(
            "pet_form.html", form=form)
