import urllib.request
import json
from .models import Source, Article
from .main import main

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    """
    retrieves all the sources
    """
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        results = None
        if sources_response['sources']:
            results= process_response(sources_response['sources'])
    return results

def get_leading_articles_by_source(source):

    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources=%s&apiKey=%s' % (source, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        results = None
        if article_response['totalResults'] > 0:
            results = process_article_response(article_response['articles'])
    return results

def process_article_response(articles):
    results_list = []

    for article_item in articles:
        author = article_item.get('author')
        title = article_item.get('title')
        desc = article_item.get('description')
        image = article_item.get('urlToImage')
        url = article_item.get('url')

        article_object = Article(author, title, desc, image, url)
        results_list.append(article_object)
    return results_list
    
def process_response(response):
    results_list = []

    for response_item in response:
        id = response_item.get('id')
        name = response_item.get('name')
        desc = response_item.get('description')
        url = response_item.get('url')
        country = response_item.get('country')

        response_object = Source(id, name, desc, country, url)
        results_list.append(response_object)
    return results_list
