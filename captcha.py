class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = leftOperand
		self.operator = operator
		self.rightOperand = rightOperand

	def left_operand(self):
		if self.pattern == 2:
			if self.leftOperand == 2:
				return "two"
			if self.leftOperand == 3:
				return "three"
			if self.leftOperand == 4:
				return "four"
			return "one"
		return str(self.leftOperand)