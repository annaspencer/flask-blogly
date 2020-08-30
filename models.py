"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__= 'users'

    def __repr__(self):
        u =self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

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
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

    def get_full_name(self):
        u = self
        return f"{u.first_name} {u.last_name}"