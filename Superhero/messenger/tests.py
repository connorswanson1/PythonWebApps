from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Message


def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())


class MessageDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.person = dict(user=self.user, bio='single tester')
        self.message1 = dict(user=self.user)



class MessageViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        #self.user, self.user_args = create_test_user()
        self.message1 = dict(title='Doc Title 1', body='Doc Body 1')
        self.message2 = dict(title='Doc Title 2', body='Doc Body 2')

