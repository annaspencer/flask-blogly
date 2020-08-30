"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = "891-327-672"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug =True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def index():
    """Redirects to Users list, per instructions."""

    return redirect("/users")


@app.route("/users")
def users():
    """users page"""

    return render_template("/users.html")

@app.route('/create_user', methods=["GET"])
def create_user():
    """Return create user page."""

    return render_template("/create-user.html")


# @app.route('/user_details')
# def user_details():
#     """Return user details."""

#     return render_template("/user-details.html")

# @app.route('/user_edit')
# def user_edit():
#     """Return edit user"""

#     return render_template("/user-edit.html")
