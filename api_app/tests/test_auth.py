from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()


class AuthTests(TestCase):
    fixtures = ['auth.json']
    credentials_valid = {'username': 'admin', 'password': 'admin'}

    def test_login_api(self):
        response = client.post('/api/auth/login/', self.credentials_valid)
        self.assertEqual(response.status_code, 200)
        self.assertIsNot(response.data['token'], '')
