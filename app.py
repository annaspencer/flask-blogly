"""Blogly application."""

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = "891-327-672"
debug = DebugToolbarExtension(app)
app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def index():
    """Return homepage."""

    return render_template("base.html")
