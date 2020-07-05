class Source:
    """
    initialization
    """
    all_sources = []
    def __init__(self, id, name, desc, country, url):
        self.id = id
        self.name = name
        self.description = desc
        self.country = country
        self.url = url

    def save_source(self):
        self.all_sources.append(self)

class Article:
    
    all_articles = []

    def __init__(self, author, title, desc, urlImg, urlArt, source):

        self.author = author
        self.title = title
        self.description = desc
        self.urlToImage = urlImg
        self.url = urlArt
        self.source = source

    def save_article(self):
        self.all_articles.append(self)