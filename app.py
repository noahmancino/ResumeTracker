from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Boostrap

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
