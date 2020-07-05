from flask import render_template, redirect, url_for, request
from . import main
from ..requests import get_sources, get_leading_articles_by_source, search_article_keyword


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
    keyword = request.args.get('keyword')
    language = request.args.get('language')
    if keyword or language:
        return redirect(url_for('main.everything_search', keyword=keyword, language=language))
    else:
        return render_template('everything.html', title= title)
    

@main.route('/headline/<source>')
def headline_source(source):
    headlines = get_leading_articles_by_source(source)
    message= 'Headlines for %s' % source.capitalize()
    return render_template('sourceHeadline.html', headlines = headlines, message = message)

@main.route('/everything/article/<keyword>&<language>')
def everything_search(keyword, language):
    new_keyword = '+'.join(keyword.split(' '))
    searched_articles = search_article_keyword(new_keyword, language)
    message = "Here are the first 15 articles with %s" % keyword
    return render_template('everything.html', searched_articles=searched_articles, message=message)

