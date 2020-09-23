#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/python15h/')
def hello_python15h():
    return 'Welcome to python15h!'

if __name__ == '__main__':
    app.run()