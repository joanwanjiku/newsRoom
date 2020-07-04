import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    """
    test case for source class
    """
    def setUp(self):
        """
        runs before each testcase
        """
        self.new_source = Source('abc-news', 'ABC News', 'Trusted source for breaking news', 'us', 'https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_save_source(self):
        self.new_source.save_source()
        self.assertEqual(len(Source.all_sources), 1)

    