from unittest import TestCase
from tests.client import Request
from server.Server import Server


class TestConnection(TestCase):
    def test_conn_unavailable(self):
        self.assertEqual(Request.request('request_body'), 'can\'t connect to server')
