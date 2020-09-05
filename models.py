"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__= 'users'

    

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.String(50),
                            nullable=False,
                            unique=False)

    last_name = db.Column(db.String(50),
                            nullable=False,
                            unique=False)

    image_url = db.Column(db.String(50),
                            nullable=False,
                            unique=True)

    def __repr__(self):
        u =self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"    

    def get_full_name(self):
        u = self
        return f"{u.first_name} {u.last_name}"


class Post(db.Model):
    __tablename__='posts'


    id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)

    title = db.Column(db.Text, 
                            nullable=False,
                            unique=True)

    content = db.Column(db.Text,
                            nullable=False)

    created_at = db.Column(db.Text,
                            nullable=False)   

    author_code = db.Column(db.Integer, 
                            db.ForeignKey('users.id'))

    author = db.relationship('User', backref='posts')

    assignments = db.relationship('PostTag', backref='post')

    tags = db.relationship(
        'Tag', secondary="posts_tags", backref="posts")
    
    def __repr__(self):
        p =self
        return f"<Post id={p.id} title={p.title} content={p.content} author_code={p.author_code}>"

    def get_all_posts():
        all_posts = Post.query.all()

        for post in all_posts:
            print(post.title, post.author.first_name)
    
class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)

    tag_name = db.Column(db.Text, nullable=False, unique=True)

    # posts = db.relationship(
    #     'Post',
    #     secondary="posts_tags",
    #     # cascade="all,delete",
    #     backref="tags",
    # )
   
class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)

    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), primary_key=True)
