from flask import render_template
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    title = 'Home'
    sources = get_sources()    
    print(sources)
    return render_template('index.html', title=title, source= sources)

@main.route('/headline')
def headline():
    title = 'Headline'
    return render_template('headline.html', title=title)

@main.route('/everything')
def everything():
    title = 'Everything'
    return render_template('everything.html', title= title)

