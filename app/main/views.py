from flask import render_template, redirect, url_for
from . import main
from ..requests import get_sources, get_leading_articles_by_source

@main.route('/')
def index():
    title = 'Home'
    sources = get_sources()    
    return render_template('index.html', title=title, source= sources)

@main.route('/headline')
def headline():
    title = 'Headline'
    return render_template('headline.html', title=title)

@main.route('/everything')
def everything():
    title = 'Everything'
    return render_template('everything.html', title= title)

@main.route('/headline/<source>')
def headline_source(source):
    headlines = get_leading_articles_by_source(source)
    print(headlines)

    return render_template('sourceHeadline.html', headlines = headlines)
