class Source:
    '''
    source class to define the source objects
    '''

    def __init__(self, id, category, name, url, description):
        '''
        __init__ method to define the properties of a source object
        '''
        self.id = id
        self.category = category
        self.name = name
        self.url = url
        self.description = description


class Article:
	'''
	article class to define the article objects
	'''

	def __init__(self, title, description, url, image, published):
		'''
		__init__ method to define the properties of article objects

		'''
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.published = published
