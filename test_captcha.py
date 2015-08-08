import unittest
from captcha import Captcha

class TestCaptchaFirstPatternLeftOperand(unittest.TestCase):
	firstPattern = 1
	dummyOperator = 1
	dummyRightOperand = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.firstPattern, 1, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('1', captcha.left_operand())

	def test_2_should_be_2(self):
		captcha = Captcha(self.firstPattern, 2, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('2', captcha.left_operand())

class TestCaptchaSecondPatternLeftOperand(unittest.TestCase):
	secondPattern = 2
	dummyOperator = 1
	dummyRightOperand = 1

	def test_1_should_be_one(self):
		captcha = Captcha(self.secondPattern, 1, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('one', captcha.left_operand())

	def test_2_should_be_two(self):
		captcha = Captcha(self.secondPattern, 2, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('two', captcha.left_operand())

	def test_3_should_be_three(self):
		captcha = Captcha(self.secondPattern, 3, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('three', captcha.left_operand())

	def test_4_should_be_three(self):
		captcha = Captcha(self.secondPattern, 4, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('four', captcha.left_operand())

class TestCaptchaSecondPatternLeftOperand(unittest.TestCase):
	secondPattern = 1
	dummyOperator = 1
	dummyLeftOperand = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 1)
		self.assertEqual('1', captcha.right_operand())

	def test_2_should_be_2(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 2)
		self.assertEqual('2', captcha.right_operand())




