from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.messages import get_messages
from django.core import mail
from django.urls import reverse
from django.contrib.auth import login
from main.models import Topic, Report
from django.utils import timezone
#from .views import welcome_email, register_request, login_request, logout_request


class ReportTestCase(TestCase):

    def setUp(self):
        # Create a user and topic for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.topic = Topic.objects.create(name='testtopic')
        self.report = Report.objects.create(
            report='test report',
            user_id=self.user,
            topic=self.topic,
            date_created='2024-05-15 09:54:51.031313'
        )

    def test_report_create(self):
        data = {
            "report": 'test report',
            "user_id": self.user,
            "topic": self.topic,
            "date_created": '2024-05-15 09:54:51.031313'
        }
        response = self.client.post(reverse('main:report'), data)
        print('report create')
        print("response.status_code = ", response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_report_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('manager:report_delete', kwargs={'id': self.report.id}))
        self.assertEqual(response.status_code, 302)
        print("report delete")
        with self.assertRaises(Report.DoesNotExist):
            Report.objects.get(id=self.report.id)


