from flask import Flask, render_template, redirect, url_for, request
import jinja2
import const

app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('application/welcome.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
