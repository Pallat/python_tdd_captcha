import unittest
from app import app

class TestFizzBuzzAPI(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_root(self):
		response = self.app.get('/')
		self.assertEqual(404, response.status_code)

	def test_route_captcha(self):
		response = self.app.get('/captcha')
		self.assertEqual(200, response.status_code)
