class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = leftOperand
		self.operator = operator
		self.rightOperand = rightOperand

	def left_operand(self):
		map_number = {1:"one", 2:"two", 3:"three", 4:"four"}
		if self.pattern == 2:
			return map_number[self.leftOperand]
		return str(self.leftOperand)