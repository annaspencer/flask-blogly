"""Seed file to make test users"""

from models import User, Post, db
from app import app

#create all tables
db.drop_all()
db.create_all()

#If table isn't empty, then empty it
User.query.delete()
Post.query.delete()

#add users

anna = User(first_name="Anna", last_name="Spencer", image_url="https://unsplash.com/photos/B4GLLQVIdLQ")
charlie = User(first_name="Charlie", last_name="Spencer", image_url="https://unsplash.com/photos/Wlkwxi2kNP0")
emma = User(first_name="Emma", last_name="James", image_url="https://unsplash.com/photos/d4eX55qjSq0")
buck= User(first_name="Buck", last_name="Spencer", image_url="https://unsplash.com/photos/4vIJuuJE5pQ")

#add posts
title1 = Post(title="Post Title", content="Some content here about something.", created_at="created at a time function that hasn't been created.", author_code=1)
title2 = Post(title="Post Title2", content="Some content here about something2.", created_at="created at a time function that hasn't been created.", author_code=1)
title3 = Post(title="Post Title3", content="Some content here about something3.", created_at="created at a time function that hasn't been created.", author_code=2)
title4 = Post(title="Post Title4", content="Some content here about something4.", created_at="created at a time function that hasn't been created.", author_code=2)
title5 = Post(title="Post Title5", content="Some content here about something5.", created_at="created at a time function that hasn't been created.", author_code=3)
title6 = Post(title="Post Title6", content="Some content here about something6.", created_at="created at a time function that hasn't been created.", author_code=3)
title7 = Post(title="Post Title7", content="Some content here about something7.", created_at="created at a time function that hasn't been created.", author_code=4)
title8 = Post(title="Post Title8", content="Some content here about something8.", created_at="created at a time function that hasn't been created.", author_code=4)

#add to db
db.session.add(anna)
db.session.add(charlie)
db.session.add(emma)
db.session.add(buck)

db.session.commit()

db.session.add(title1)
db.session.add(title2)
db.session.add(title3)
db.session.add(title4)
db.session.add(title5)
db.session.add(title6)
db.session.add(title7)
db.session.add(title8)

#db commit
db.session.commit()