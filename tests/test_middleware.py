from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpRequest, HttpResponse
from django.test import TestCase, override_settings

from rest_framework.test import APIClient

import base64

from abac.middleware import ABACMiddleware


def simple_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse('OK', status=200)
    return HttpResponse('Bad', status=403)


urlpatterns = [
    url(r'^post$', simple_view, name='simple_view'),
]


@override_settings(ROOT_URLCONF='tests.test_middleware')
class ABACMiddlewareTests(TestCase):
    """ Test the ``UserenaLocaleMiddleware`` """
    # fixtures = ['users', ]

    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    @staticmethod
    def _get_request_with_user(user):
        """ Fake a request with an user and basic authentication """
        request = HttpRequest()
        request.META = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(
                '{username}:{password}'.format(
                    username=user.username,
                    password='top_secret',
                ).encode()).decode(),
        }
        request.method = 'GET'
        request.session = {}

        # Add user
        request.user = user
        return request

    def test_basic_authorization(self):
        request = self._get_request_with_user(self.user)
        auth_user = ABACMiddleware(None).get_auth_user(request)
        self.assertEqual(self.user, auth_user)

    def test_view_user_is_basic_authentication(self):
        simple_view_url = reverse('simple_view')
        request = self._get_request_with_user(self.user)
        response = self.client.get(simple_view_url, **request.META)
        self.assertEqual(response.status_code, 200)

    def test_view_user_is_anonymous(self):
        simple_view_url = reverse('simple_view')
        response = self.client.get(simple_view_url)
        self.assertEqual(response.status_code, 403)
