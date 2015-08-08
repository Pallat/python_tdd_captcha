import json
from random import randint

class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = self.operandSelector(pattern,leftOperand)
		invert = 1
		if pattern == 1:
			invert = 2
		self.rightOperand = self.operandSelector(invert,rightOperand)
		self.operator = Operator(operator)

	def operandSelector(self,pattern,operand):
		if pattern == 2:
			return StringOperand(operand)
		return NumberOperand(operand)

class Operator:
	def __init__(self, operator):
		self.operator = operator
		self.map_operator = {1:"+", 2:"*", 3:"-"}

	def toString(self):
		return self.map_operator[self.operator]

class StringOperand:
	def __init__(self,operand):
		self.operand =operand
		self.map_number = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}

	def toString(self):
		return self.map_number[self.operand]

class NumberOperand:
	def __init__(self,operand):
		self.operand =operand

	def toString(self):
		return str(self.operand)

class Randomizer:
	def pattern(self):
		return randint(1,2)
	def operand(self):
		return randint(1,9)
	def operator(self):
		return randint(1,3)

class Output:
	def __init__(self, captcha):
		self.captcha = captcha
	def json(self):
		obj = {"left": self.captcha.leftOperand.toString(), "operator": self.captcha.operator.toString(), "right": self.captcha.rightOperand.toString()}
		# obj = {"left": "1", "operator": "1", "right": "1"}
		return json.dumps(obj)

class CaptchaController:
	def __init__(self):
		self.random = Randomizer()
	def toJson(self):
		pattern = self.random.pattern()
		leftOperand = self.random.operand()
		operator = self.random.operator()
		rightOperand = self.random.operand()
		captcha = Captcha(pattern, leftOperand, operator, rightOperand)
		# captcha = Captcha(2, 1, 1, 1)
		output = Output(captcha)
		return output.json()


