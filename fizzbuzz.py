class FizzBuzz:
	def count(self,number):
		isModulo3 = number%3 == 0
		isModulo5 = number%5 == 0

		if isModulo3 and isModulo5:
			return "fizzbuzz"
		if isModulo3:
			return "fizz"
		if isModulo5:
			return "buzz"
		return str(number)
