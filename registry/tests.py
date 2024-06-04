from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.messages import get_messages
from django.core import mail
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth import login
#from .views import welcome_email, register_request, login_request, logout_request


class RegisterTestCase(TestCase):
    def test_register(self):
        print("test name: test_register")
        data = {
            "username": 'testuser',
            "email": 'test@gmail.com',
            "password": 'testpassword',
            "password2": 'testpassword'
        }
        response = self.client.post(reverse('registry:register'), data)
        self.assertEqual(response.status_code, 200)


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        print("test name: test_login")
        user = User.objects.create_user(username='testuser', password='testpassword')
        print("user = ", user)
        data = {
            "username": 'testuser',
            "password": 'testpassword'
        }
        response = self.client.post(reverse('registry:login'), data)
        self.assertEqual(response.status_code, 302)


    def test_logout(self):
        print("test name: test_logout")
        self.test_login()
        response = self.client.post(reverse('registry:logout'))
        self.assertEqual(response.status_code, 302)

    def test_email(self):
        print("test name: test_email")
        user = User.objects.create_user(username='testuser', email='test@gmail.com', password='testpassword')
        print("user = ", user)
        data = {
            "username": 'testuser',
            "email": 'test@gmail.com',
            "password": 'testpassword'
        }
        response = self.client.post(reverse('registry:welcome_email'))
        print("response.status_code = ", response.status_code)
        self.assertEqual(response.status_code, 302)
