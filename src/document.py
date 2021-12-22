import nltk
from nltk.corpus import stopwords

class Document:
	def __init__(self, id, title, abstract):

		self.id = id
		self.title = title
		self.abstract = abstract

	def tokenise(self):
		self.words = nltk.word_tokenize(self.title + ' ' + self.abstract)
		self.words = [word.lower() for word in self.words if word.isalnum()]

		self.frequency = {}
		for word in self.words:
			if word in stopwords.words('english') or word.isspace() or word == "":
				continue
			if word in self.frequency:
				self.frequency[word] += 1
			else:
				self.frequency[word] = 1

		return self.frequency
