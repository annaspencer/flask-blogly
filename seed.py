"""Seed file to make test users"""

from models import User, db
from app import app

#create all tables
db.drop_all()
db.create_all()

#If table isn't empty, then empty it
User.query.delete()

#add users

anna = User(first_name="Anna", last_name="Spencer", image_url="https://unsplash.com/photos/B4GLLQVIdLQ")
charlie = User(first_name="Charlie", last_name="Spencer", image_url="https://unsplash.com/photos/Wlkwxi2kNP0")
emma = User(first_name="Emma", last_name="James", image_url="https://unsplash.com/photos/d4eX55qjSq0")
buck= User(first_name="Buck", last_name="Spencer", image_url="https://unsplash.com/photos/4vIJuuJE5pQ")

#add to db
db.session.add(anna)
db.session.add(charlie)
db.session.add(emma)
db.session.add(buck)

#db commit
db.commit()