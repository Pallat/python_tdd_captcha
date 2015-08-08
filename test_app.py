import unittest
from app import app

class TestFizzBuzzAPI(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_root(self):
		response = self.app.get('/')
		self.assertEqual(200, response.status_code)
		self.assertEqual('Hello World', response.data)

	def test_fizzbuzz_return_default(self):
		response = self.app.get('/fizzbuzz/1')
		self.assertEqual('1', response.data)
		response = self.app.get('/fizzbuzz/4')
		self.assertEqual('4', response.data)

	def test_fizzbuzz_return_fizz(self):
		response = self.app.get('/fizzbuzz/3')
		self.assertEqual('fizz', response.data)
		response = self.app.get('/fizzbuzz/6')
		self.assertEqual('fizz', response.data)

	def test_fizzbuzz_return_buzz(self):
		response = self.app.get('/fizzbuzz/5')
		self.assertEqual('buzz', response.data)
		response = self.app.get('/fizzbuzz/10')
		self.assertEqual('buzz', response.data)

	def test_fizzbuzz_return_fizzbuzz(self):
		response = self.app.get('/fizzbuzz/15')
		self.assertEqual('fizzbuzz', response.data)
		response = self.app.get('/fizzbuzz/30')
		self.assertEqual('fizzbuzz', response.data)

	def test_route_captcha(self):
		response = self.app.get('/captcha')
		self.assertEqual(200, response.status_code)