import json

from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class Client(APIClient):
    def patch(
        self,
        path,
        data=None,
        format=None,
        content_type='application/json',
        follow=False,
        **extra,
    ):
        if content_type == 'application/json':
            data = json.dumps(data)
        return super(Client, self).patch(
            path,
            data,
            format,
            content_type,
            follow,
            **extra,
        )


class TestCase(APITestCase):
    client_class = Client
