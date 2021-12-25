import nltk

class Document:

	DOCUMENTS = []
	STOPWORDS = []

	def __init__(self, id, title, abstract):

		self.id = id
		self.title = title
		self.abstract = abstract

	def __str__(self):
		return str(self.id)

	def __repr__(self):
		return str(self)

	def tokenise(self):
		words = nltk.word_tokenize(self.title + ' ' + self.abstract)
		words = [word.lower() for word in words if (word not in Document.STOPWORDS and not word.isspace() and word != "")]

		self.frequency = {}
		for word in words:
			if word in self.frequency:
				self.frequency[word] += 1
			else:
				self.frequency[word] = 1
		self.words = [*self.frequency]
		return self.frequency

	def max_frequency(self):
		return max(self.frequency.values())

	def word_exist(self, word):
		return word in self.words

	@classmethod
	def nb_documents(cls):
		return len(cls.DOCUMENTS)

	@classmethod
	def all_words(cls):
		words = []
		for document in cls.DOCUMENTS:
			for word in document.words:
				if word not in words:
					words.append(word)
		return words
