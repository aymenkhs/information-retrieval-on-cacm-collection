import math

from src.read_file import *
from src.document import Document

def indexation():
	Document.STOPWORDS = read_stop_list()
	read_docs(read_file(DOCUMENT_FILE_PATH))
	for document in Document.DOCUMENTS:
		document.tokenise()
	return Document.DOCUMENTS

def inverse_file():
	words = Document.all_words()
	inverse_structure = {}
	for word in words:
		inverse_structure[word] = []
		for document in Document.DOCUMENTS:
			if word in document.words:
				inverse_structure[word].append((document, document.frequency[word]))
	return inverse_structure

def tf_idf(inverse_structure):
	weight = lambda ti, dj: (dj.frequency[ti]/dj.max_frequency()) * math.log10(Document.nb_documents()/len(inverse_structure[ti]) + 1)

	words = Document.all_words()

	inverse_weight_matrix = {}
	for word in words:
		inverse_weight_matrix[word] = []
		for document in Document.DOCUMENTS:
			if word in document.words:
				inverse_weight_matrix[word].append((document, weight(word, document)))
	return inverse_weight_matrix

def get_weight(inverse_weight_matrix, searching_document, word):
	pair_documents = inverse_weight_matrix[word]
	for document, weight in pair_documents:
		 if document.id == searching_document.id:
			 return weight
	return None
