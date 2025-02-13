from .models.user.user import User
from django.test import TestCase


class UserAuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", username="testuser")

    def test_set_password(self):
        new_password = "new_password_123"
        self.user.set_password(new_password)
        self.assertTrue(self.user.check_password(new_password))

    def test_user_auth_creation(self):
        self.assertIsNotNone(self.user.auth)
