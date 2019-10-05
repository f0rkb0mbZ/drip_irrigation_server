import unittest
from app import app

class test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_getdatanow(self):
        response = self.app.get('/getdata/now', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_getthreshold(self):
        response = self.app.get('/getthreshold', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        pass
