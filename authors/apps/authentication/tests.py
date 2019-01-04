from django.test import TestCase
from .models import UserManager,User
import pytest

class ModelTestCase(TestCase):
    """This class defines the test suite for the user manager model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.username = 'Douglas'
        self.email = 'daglach7@gmail.com'
        self.password = '12345'
        self.usermanager = UserManager()

    def test_create_user(self):
        """Test for successful creation of a user."""
        with pytest.raises(TypeError):
           user = self.usermanager.create_user(username=None, email=self.email, password=self.password)
            
 
