#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/pow/<int:x>/<int:y>/')
def web_pow(x, y):
    return '{0}'.format(pow(x, y))

if __name__ == '__main__':
    app.run()