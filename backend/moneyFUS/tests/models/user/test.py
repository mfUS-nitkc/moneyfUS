from ....utils.hash_password import hash_password
from ....models.user.user import User
from django.test import TestCase
import django.core.exceptions as Exceptions

USER = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "p4ssw0rd"
}

class UserAuthTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email=USER["email"], username=USER["username"], password=USER["password"])
        
    def test_user_name(self):
        self.assertEqual(self.user.username, USER["username"])
    
    def test_user_email(self):
        self.assertEqual(self.user.email, USER["email"])
        
    def test_user_is_not_superuser(self):
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)
    
    def test_user_is_active(self):
        self.assertEqual(self.user.is_active, True)

    def test_set_password(self):
        new_password = "new_password_123"
        self.user.set_password(new_password)
        self.assertTrue(self.user.check_password(new_password))

    def test_user_does_not_exist(self):
        u = None
        try:
            u = User.objects.get(email="non-exist@example.com")
        except User.DoesNotExist:
            pass
        if u is not None:
            TestCase.fail(self)
            
    def test_user_does_not_duplicate(self):
        u = None
        try:
            u = User.objects.create(email=USER["email"], username=USER["username"], password=USER["password"])
        except Exceptions.ValidationError:
            pass
        if u is not None:
            TestCase.fail(self)
