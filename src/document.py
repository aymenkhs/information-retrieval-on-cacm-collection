import nltk

class Document:

	def __init__(self, id, title, abstract):

		self.id = id
		self.title = title
		self.abstract = abstract

	def tokenise(self):
		self.words = nltk.word_tokenize(self.title + ' ' + self.abstract)
	    words = [word.lower() for word in words if word.isalnum()]

	    self.frequency = {}
	    for word in self.words:
	        if word in stopwords.words('english') or word.isspace() or word == "":
	            continue

	        if word in document:
	            self.frequency[word] += 1
	        else:
	            self.frequency[word] = 1


	    return self.frequency
