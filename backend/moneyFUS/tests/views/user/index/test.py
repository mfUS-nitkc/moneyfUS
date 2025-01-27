from .....models.user.user import User
from rest_framework.test import APIRequestFactory, APITestCase, APIClient

TEST_USER = {
  "username": "test",
  "email": "test@example.com",
  "password": "testpass"
}

TEST_USER_Extra = {
  "username": "extra_test",
  "email": "extra_test@example.com",
  "password": "extrapass",
  "birthday": "2005-03-18"
}

TEST_USER_2 = {
  "username": "user",
  "email": "user@example.com",
  "password": "userpass"
}

TEST_USER_FAILED_LACK = {
  "username": "user",
  "email": "user@example.com"
}

TEST_USER_NUMBERED = {
  "username": 12345,
  "email": "invalid@example.com",
  "password": "testpass" 
}

class UserIndexViewTests(APITestCase):
  def setUp(self):
    self.user = User.objects.create_user(username="test", email="test@example.com", password="testpass")
    self.client = APIClient()
    self.client.force_authenticate(self.user)
    
  def test_create_user(self):
    response = self.client.post("/api/v1/user", TEST_USER_2)
    self.assertEqual(response.status_code, 201)
    self.assertTrue(response.data["success"])                               # 成功している
    self.assertEqual(response.data["username"], TEST_USER_2["username"])    # ユーザー名が返される
    self.assertEqual(response.data["email"], TEST_USER_2["email"])          # メールアドレスが返される
    self.assertNotIn("password", response.data)                             # パスワードは漏洩していない
  
  def test_create_user_extra(self):
    response = self.client.post("/api/v1/user", TEST_USER_Extra)
    self.assertEqual(response.status_code, 201)
    self.assertTrue(response.data["success"])                                 # 成功している
    self.assertEqual(response.data["username"], TEST_USER_Extra["username"])  # ユーザー名が返される
    self.assertEqual(response.data["email"], TEST_USER_Extra["email"])        # メールアドレスが返される
    self.assertNotIn("birthday", response.data)                               # 変なフィールドは帰ってこない
    self.assertNotIn("password", response.data)                               # パスワードは漏洩していない
    
  def test_failed_create_user(self):
    response = self.client.post("/api/v1/user", TEST_USER_FAILED_LACK)
    self.assertEqual(response.status_code, 400)
    self.assertFalse(response.data["success"])
    self.assertEqual(response.data["reason"], "Invalid Type or Parameter")
    
  def test_failed_create_invalid_type(self):
    response = self.client.post("/api/v1/user", TEST_USER_NUMBERED)
    self.assertEqual(response.status_code, 201)
    self.assertTrue(response.data["success"])
    self.assertEqual(response.data["username"], str(TEST_USER_NUMBERED["username"]))
    self.assertEqual(response.data["email"], TEST_USER_NUMBERED["email"])
    self.assertNotIn("password", response.data)
    
  def test_failed_create_duplicated_user(self):
    response = self.client.post("/api/v1/user", TEST_USER)
    self.assertEqual(response.status_code, 400)
    self.assertFalse(response.data["success"])
    self.assertEqual(response.data["reason"], "Duplicated User")
    
  def test_user_delete(self):
    response = self.client.delete("/api/v1/user")
    self.assertEqual(response.status_code, 204)
    
  def test_failed_user_delete(self):
    self.client.logout()
    response = self.client.delete("/api/v1/user")
    self.assertEqual(response.status_code, 401)
