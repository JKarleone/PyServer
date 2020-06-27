from unittest import TestCase
from tests.client import Request
from server.Server import Server


class TestConnection(TestCase):
    def test_conn_unavailable(self):
        self.assertEqual(Request.request('request_body'), 'can\'t connect to server')


class TestServer(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = Server()
        cls.server.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.stop()

    def test_wrong_table(self):
        self.assertEqual(Request.request('request_body'), 'error')

    def test_empty_body(self):
        self.assertEqual(Request.request(''), 'error')

    def test_lack_of_2_param(self):
        self.assertEqual(Request.request('film'), 'params error')
        self.assertEqual(Request.request('reg'), 'params error')
        self.assertEqual(Request.request('auth'), 'params error')
        self.assertEqual(Request.request('score'), 'params error')

    def test_unavailable_method(self):
        self.assertEqual(Request.request('score&add&5&3&my_title'), 'error')