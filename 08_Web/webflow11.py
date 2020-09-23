#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def from_index():
    if request.method == 'POST':
        if 'text1' in request.form:
            return render_template('webflow11.html', text1=request.form['text1'])
    return render_template('webflow11.html')

if __name__ == '__main__':
    app.run(debug=True)