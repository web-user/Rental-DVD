from django.test import TestCase

from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase


from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='vld', email='hello@vld.com')
        user.set_password("yeahhhvld")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='vld')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'vld.doe',
            'email': 'vld.doe@gmail.com',
            'password': 'learncode',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # 400
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'vld.doe',
            'email': 'cfe.doe@gmail.com',
            'password': 'learncode',
            'password2': 'learncode'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 400
        token_len = len(response.data.get("token", 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'vld',
            'password': 'yeahhhvld',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)
