import unittest
from captcha import Captcha

class TestCaptchaFirstPatternLeftOperand(unittest.TestCase):
	def test_1_should_be_1(self):
		captcha = Captcha(1, 1, 1, 1)
		self.assertEqual('1', captcha.left_operand())

	def test_2_should_be_2(self):
		captcha = Captcha(1, 2, 1, 1)
		self.assertEqual('2', captcha.left_operand())

class TestCaptchaSecondPatternLeftOperand(unittest.TestCase):
	def test_1_should_be_one(self):
		captcha = Captcha(2, 1, 1, 1)
		self.assertEqual('one', captcha.left_operand())

	def test_2_should_be_two(self):
		captcha = Captcha(2, 2, 1, 1)
		self.assertEqual('two', captcha.left_operand())