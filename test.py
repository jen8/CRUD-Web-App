import json
from unittest import TestCase
from model import Courses, Student, connect_to_db, db
from server import app



class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_display_post(self):
        """Test home page."""

        result = self.client.get("/home")
        self.assertIn("Welcome", result.data)




class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        

    def test_make_post_page(self):
        """Test make posts page."""

        
        result = self.client.get("/create")
        self.assertIn("Create Student", result.data)






if __name__ == "__main__":
    import unittest
    connect_to_db(app)

    unittest.main()