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