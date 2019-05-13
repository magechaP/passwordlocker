import unittest
from user import User
from credential import credentials
import pyperclip


class TestUser(unittest.TestCase):
    """
    test class that defines test cases for the user class behaviours
    """
    def setUp(self):
        """
        set up method to run before each test case
        """
        self.new_user = User("facebook","manka","2999") # crreate user objects