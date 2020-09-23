#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pow/<int:x>/<int:y>/')
def web_pow(x, y):
    result = pow(x, y)
    return render_template('webflow05.html', x=x, y=y, result=result)

if __name__ == '__main__':
    app.run()