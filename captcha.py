from random import randint

class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = self.operandSelector(pattern,leftOperand)
		self.rightOperand = self.operandSelector(pattern,rightOperand)
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