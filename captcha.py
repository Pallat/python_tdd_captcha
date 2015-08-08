class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = leftOperand
		self.operator = operator
		self.rightOperand = rightOperand
		self.map_number = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}

	def left_operand(self):
		if self.pattern == 2:
			return self.map_number[self.leftOperand]
		return str(self.leftOperand)

	def right_operand(self):
		if self.pattern == 2:
			return self.map_number[self.rightOperand]
		return str(self.rightOperand)

	def operator_flag(self):
		if self.operator == 2:
			return '-'
		return '+'

