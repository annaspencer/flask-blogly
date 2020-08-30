from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample user."""

        User.query.delete()

        elton = User(first_name="Elton", last_name="John", image_url="https://unsplash.com/photos/fr8yMGRS_X8")
        db.session.add(elton)
        db.session.commit()

        self.user_id = elton.id
        self.user = elton

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Elton', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Elton</h1>', html)
            self.assertIn(self.user.first_name, html)
            

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name":"Marshall", "last_name":"Mathers", "image_url":"https://unsplash.com/photos/fr8yMGRS_X8"}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Marshall</h1>", html)
