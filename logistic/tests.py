from unittest import TestCase

from rest_framework.test import APIClient


class TestSomething(TestCase):
    def test_sample_view(self):
        client = APIClient()
        response = client.get('/api/v1/test/')
        self.assertEqual(response.status_code, 200)

def test_bad_case(self):
        client = APIClient()
        response = client.get('/api/v1/test/')
        self.assertEqual(response.status_code, 404)
