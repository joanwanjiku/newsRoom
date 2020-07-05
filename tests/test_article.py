import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):

    """
    tests for the class Article
    """
    def setUp(self):
        """
        run before each test
        """
        self.new_article = Article('bbc news', 'Two hurt as car strikes protest in Seattle', 
        'The women are seriously injured as the vehicle careers into protesters on a closed highway', 
        'https://ichef.bbci.co.uk/news/1024/branded_news/8600/production/_113240343_gettyimages-1223820095.jpg',
        '"http://www.bbc.co.uk/news/world-us-canada-53291289', 'bbc'
        )
        
    def test_init(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_save_article(self):
        self.new_article.save_article()
        self.assertEqual(len(Article.all_articles), 1)