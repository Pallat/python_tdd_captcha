from flask import Flask
from fizzbuzz import FizzBuzz

app = Flask(__name__)

@app.route('/')
def root():
	return "Hello World"

@app.route('/fizzbuzz/<int:number>')
def fizzbuzz(number):
	fb = FizzBuzz()
	return fb.count(number)

if __name__ == '__main__':
	app.run()