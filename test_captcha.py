import unittest
from captcha import Captcha
from captcha import Operator
from captcha import StringOperand
from captcha import NumberOperand
from captcha import Randomizer
from captcha import Output

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

class TestStringOperand(unittest.TestCase):
	def test_1_should_be_one(self):
		operand = StringOperand(1)
		self.assertEqual('one', operand.toString())

class TestNumberOperand(unittest.TestCase):
	def test_1_should_be_1(self):
		operand = NumberOperand(1)
		self.assertEqual('1', operand.toString())

class TestRandomizerPattern(unittest.TestCase):
	def test_pattern_should_not_more_than_2(self):
		random = Randomizer()
		self.assertTrue(random.pattern() <= 2)
		self.assertTrue(random.pattern() >= 1)

class TestRandomizerOperand(unittest.TestCase):
	def test_operand_should_in_range_1_to_9(self):
		random = Randomizer()
		self.assertTrue(random.operand() >= 1)
		self.assertTrue(random.operand() <= 9)

class TestOutput(unittest.TestCase):
	def test_get_json(self):
		captcha = Captcha(1,1,1,1)
		output = Output(captcha)
		self.assertEqual('{"operator": "+", "right": "1", "left": "1"}', output.json())





