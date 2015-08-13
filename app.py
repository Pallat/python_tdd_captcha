from flask import Flask
from captcha import CaptchaController

app = Flask(__name__)

@app.route('/captcha')
def captcha():
	captcha = CaptchaController()
	return captcha.toJson()

if __name__ == '__main__':
	app.run()
