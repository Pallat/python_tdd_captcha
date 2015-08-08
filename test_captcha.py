import unittest
from captcha import Captcha
from captcha import Operator
from captcha import Operand

class TestCaptchaFirstPatternLeftOperand(unittest.TestCase):
	firstPattern = 1
	dummyOperator = 1
	dummyRightOperand = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.firstPattern, 1, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('1', captcha.leftOperand.toString())

	def test_2_should_be_2(self):
		captcha = Captcha(self.firstPattern, 2, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('2', captcha.leftOperand.toString())

class TestCaptchaSecondPatternLeftOperand(unittest.TestCase):
	secondPattern = 2
	dummyOperator = 1
	dummyRightOperand = 1

	def test_1_should_be_one(self):
		captcha = Captcha(self.secondPattern, 1, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('one', captcha.leftOperand.toString())

	def test_2_should_be_two(self):
		captcha = Captcha(self.secondPattern, 2, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('two', captcha.leftOperand.toString())

	def test_3_should_be_three(self):
		captcha = Captcha(self.secondPattern, 3, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('three', captcha.leftOperand.toString())

	def test_4_should_be_three(self):
		captcha = Captcha(self.secondPattern, 4, self.dummyOperator, self.dummyRightOperand)
		self.assertEqual('four', captcha.leftOperand.toString())

class TestCaptchaFirstPatternRightOperand(unittest.TestCase):
	secondPattern = 1
	dummyOperator = 1
	dummyLeftOperand = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 1)
		self.assertEqual('1', captcha.rightOperand.toString())

	def test_2_should_be_2(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 2)
		self.assertEqual('2', captcha.rightOperand.toString())


class TestCaptchaSecondPatternRightOperand(unittest.TestCase):
	secondPattern = 2
	dummyOperator = 1
	dummyLeftOperand = 1

	def test_1_should_be_one(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 1)
		self.assertEqual('one', captcha.rightOperand.toString())

	def test_2_should_be_two(self):
		captcha = Captcha(self.secondPattern, self.dummyLeftOperand, self.dummyOperator, 2)
		self.assertEqual('two', captcha.rightOperand.toString())


class TestCaptchaOperator(unittest.TestCase):
	dummyPattern = 1
	dummyLeftOperand = 1
	dummyRightOperand = 1

	def test_1_should_be_plus(self):
		captcha = Captcha(self.dummyPattern, self.dummyLeftOperand, 1, self.dummyRightOperand)
		self.assertEqual('+', captcha.operator.toString())

	def test_2_should_be_multiply(self):
		captcha = Captcha(self.dummyPattern, self.dummyLeftOperand, 2, self.dummyRightOperand)
		self.assertEqual('*', captcha.operator.toString())

	def test_3_should_be_minus(self):
		captcha = Captcha(self.dummyPattern, self.dummyLeftOperand, 3, self.dummyRightOperand)
		self.assertEqual('-', captcha.operator.toString())

class TestOperator(unittest.TestCase):
	def test_1_should_be_plus(self):
		operator = Operator(1)
		self.assertEqual('+', operator.toString())

	def test_2_should_be_multiply(self):
		operator = Operator(2)
		self.assertEqual('*', operator.toString())

	def test_3_should_be_multiply(self):
		operator = Operator(3)
		self.assertEqual('-', operator.toString())


class TestOperand(unittest.TestCase):
	def test_first_pattern_1_should_be_1(self):
		operand = Operand(1,1)
		self.assertEqual('1', operand.toString())

	def test_second_pattern_1_should_be_one(self):
		operand = Operand(2,1)
		self.assertEqual('one', operand.toString())

