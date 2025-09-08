###################################################################################################
#   100 Days of Code: The Complete Python Pro Bootcamp
#   Portfolio Assignment 02 - Portfolio Website
###################################################################################################

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

# initialise
app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


# run flask app
if __name__ == '__main__':
    app.run(debug=True)