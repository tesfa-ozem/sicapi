import os
import unittest
from blue import create_app, db
from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    TESTING = True


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


if __name__ == '__main__':
    unittest.main()
