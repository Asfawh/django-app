from django.test import TestCase
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
