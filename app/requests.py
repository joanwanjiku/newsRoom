import urllib.request
import json
from .models import Source
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
