import unittest
from app.models import Source


class TestSource(unittest.TestCase):
    '''
    Testing the behaviour of the source class
    '''

    def setUp(self):
        '''
        runs before every test
        '''
        self.new_source = Source("bbc-news-uk", "BBC NEWS", "Most trusted news source.", "http://www.bbc.co.uk/news", "news")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
		test_init test case to test if the object is initialized porperly
        '''
        self.assertEqual(self.new_source.id, "bbc-news-uk")
		    
        self.assertEqual(self.new_source.name, "BBC NEWS")
		    
        self.assertEqual(self.new_source.description, "Most trusted news source.")
        self.assertEqual(self.new_source.url, "http://www.bbc.co.uk/news")
        self.assertEqual(self.new_source.category, "news")


		
