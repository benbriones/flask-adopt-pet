import os
from flask import Flask, render_template, redirect
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///adopt')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.get('/')
def display_homepage():
    """displays the homepage, with all Pets"""
    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def display_pets_form():
    """
    GET will render add pet form
    POST will add pet to database, redirect to home"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data or None
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


@app.route("/<int:id>", methods=["GET", "POST"])
def display_edit_pet_form(id):
    """
    GET will display edit form
    POST will process edits to a pet
    """
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo = form.photo.data or None
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')

    else:
        return render_template(
            "edit_pet_form.html", form=form, pet=pet)
