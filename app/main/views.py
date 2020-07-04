from flask import render_template
from . import main

@main.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/headline')
def headline():
    title = 'Headline'
    return render_template('headline.html', title=title)

@main.route('/everything')
def everything():
    title = 'Everything'
    return render_template('everything.html', title= title)

