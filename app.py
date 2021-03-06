# import
from flask import Flask
import os
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/about-us')
def about():
    return "<h1>Hello Handsome Boy</h1>"


@app.route('/lucky')
def lucky_number():
    number = random.randint(1000, 9999)
    return "your lucky number is" + str(number)


@app.route('/starswars')
def star_wars():
    return "<h1>EMPIRE STRIKES BACK....HA!</h1>"


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
