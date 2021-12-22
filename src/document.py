import nltk
from nltk.corpus import stopwords

class Document:

	STOPWORDS = []

	def __init__(self, id, title, abstract):

		self.id = id
		self.title = title
		self.abstract = abstract

	def tokenise(self):
		words = nltk.word_tokenize(self.title + ' ' + self.abstract)
		words = [word.lower() for word in words if word.isalnum()]

		self.frequency = {}
		for word in words:
			if word in Document.STOPWORDS or word.isspace() or word == "":
				continue
			if word in self.frequency:
				self.frequency[word] += 1
			else:
				self.frequency[word] = 1
		self.words = [*self.frequency]
		return self.frequency
