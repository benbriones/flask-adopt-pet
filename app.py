import os
from flask import Flask , render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

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

    return render_template('homepage.html', pets = pets)