from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')   
def home():
    return render_template('home.template.html')

@app.route('/hello')
def greetings():
    firstname = "Christiano"
    lastname = "Ronaloo"
    today = datetime.now()
    return render_template('greetings.template.html',
                         fname=firstname,
                         lname=lastname,
                         today_date=today)

@app.route('/calculate/<weight>/<height>')
def calculate_bmi(weight, height):
    weight = float (weight)
    height = float(height)
    bmi = weight / height ** 2
    return render_template('bmi_results.template.html',
    bmi=bmi)


@app.route('/wish/<username>')
def wish_happy_new_year(username):
     return "Happy New Year 2021," + username



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
 