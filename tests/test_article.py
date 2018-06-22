import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    '''
	Test Case to test the behaviour of the Article Model
	Args:
		unittest.TestCase - helps in creating Test Cases
	'''

    def setUp(self):
        '''
        runs before every test
        '''
        self.new_article = Article("How to catch a rabbit", "Article describing efficient ways of catching rabbits", "https://rabbitCatcher.com", "https://rabbitCatcher.com/rabbit.jpg", "2018-05-13T12:37:20Z")

    def test_instance(self):
        '''
		Function to test if the object created in the setup is indeed a Source Object
		'''
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
    	'''
		test_init test case to test if the object is initialized porperly
		'''

		self.assertEqual(self.new_article.title, "How to catch a rabbit")

		
        self.assertEqual(self.new_article.description, "Article describing efficient ways of catching rabbits")
        self.assertEqual(self.new_article.url, "https://rabbitCatcher.com")
        self.assertEqual(self.new_article.image, "https://rabbitCatcher.com/rabbit.jpg")
        self.assertEqual(self.new_article.published,
                         "2018-05-13T12:37:20Z")
