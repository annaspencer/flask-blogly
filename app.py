"""Blogly application."""

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
import datetime

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
    posts = Post.query.all()
    return render_template("/user-details.html", user=user, posts=posts)

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

@app.route('/<int:user_id>/posts/new')
def create_post_form(user_id):
    user = User.query.get_or_404(user_id)

    return render_template("/create-post.html", user=user )

@app.route('/<int:user_id>/posts/new', methods=['POST'])
def add_post_form(user_id):
    user = User.query.get_or_404(user_id)
    user.posts.title = request.form['title']
    user.posts.content = request.form['content']
    created_at = datetime.datetime.now()

    new_post = Post(title=user.posts.title, content=user.posts.title, created_at=created_at, author_code=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/{user.id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Return Post details"""

    posts = Post.query.get_or_404(post_id)

    return render_template("/post-details.html", posts=posts)

@app.route('/posts/<int:post_id>/edit')
def post_edit_form(post_id):
    """Return edit post form"""
    posts = Post.query.get_or_404(post_id)
    return render_template("/edit-post.html", posts=posts)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    """Edit Post details"""

    posts = Post.query.get_or_404(post_id)
    
    posts.title = request.form['title']
    posts.content = request.form['content']
    posts.created_at = datetime.datetime.now()

    db.session.add(posts)
    db.session.commit()
    
    return render_template("/post-details.html", posts=posts)

@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    
    Post.query.filter_by(id=post_id).delete()
    
    db.session.commit()

    return redirect("/posts")  

@app.route('/posts')
def show_posts():
    """show all posts"""
    posts = Post.query.all()

    return render_template('posts.html',posts = posts)