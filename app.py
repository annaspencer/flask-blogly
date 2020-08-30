"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = "891-327-672"
# debug = DebugToolbarExtension(app)
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
    """users list page"""
    users = User.query.all()
    return render_template("/users.html", users=users)

@app.route('/create-user')
def create_user_form():
    """returns create user form."""
    

    return render_template("/create-user.html" )

@app.route('/create-user', methods=['POST'])
def created_user():
    """processes the create user form, adding a new user and going back to list."""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/{new_user.id}" )

@app.route('/<int:user_id>')
def user_details(user_id):
    """Return user details"""
    user = User.query.get_or_404(user_id)
    return render_template("/user-details.html", user=user)

@app.route('/<int:user_id>/edit')
def user_edit_form(user_id):
    """Return edit user form"""
    user = User.query.get_or_404(user_id)
    return render_template("/user-edit.html", user=user)

@app.route('/<int:user_id>/edit', methods=["POST"])
def edit(user_id):
    """edits the user on the db, returns to users list"""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.route('/<int:user_id>/delete')
def delete(user_id):
    
    User.query.filter_by(id=user_id).delete()
    
    db.session.commit()

    return redirect("/users")   